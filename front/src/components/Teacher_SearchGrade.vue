<template>
  <div>
    <div>Teacher_SearchGrade</div>
    <div>请选择以下一门课程</div>
    <el-table
      :data="tableMyTeachData"
      stripe
      fit
      style="margin: 0 auto; width: 90%; text-align:center;"
    >
      <el-table-column prop="course_id" label="课程号" width="180"></el-table-column>
      <el-table-column prop="course_name" label="课程名" width="180"></el-table-column>
      <el-table-column prop="credit" label="学分" width="180"></el-table-column>
      <el-table-column prop="course_time" label="上课时间" width="180"></el-table-column>
      <el-table-column prop="teacher_id" label="教师号" width="180"></el-table-column>
      <el-table-column prop="teacher_name" label="教师名" width="180"></el-table-column>
      <el-table-column prop="place" label="上课教室" width="180"></el-table-column>
      <el-table-column prop="cur_stu_num" label="人数" width="180"></el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button size="mini" type="success" @click="handleEdit(scope.$index, scope.row)">查看成绩</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-table
      v-show="isShow"
      :data="tableStudentGrade"
      stripe
      fit
      style="margin: 0 auto; width: 50%; text-align:center;"
    >
      <el-table-column prop="student_id" label="学号" width="180"></el-table-column>
      <el-table-column prop="student_name" label="姓名" width="180"></el-table-column>
      <el-table-column prop="routine_score" label="平时成绩" width="180"></el-table-column>
      <el-table-column prop="exam_score" label="考试成绩" width="180"></el-table-column>
      <el-table-column prop="total_score" label="总评成绩" width="180"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isShow: false,
      tableMyTeachData: [{
        course_id: '01001234',
        course_name: '编译原理',
        course_time: '周三1-2',
        teacher_id: '1000',
        teacher_name: '魏晓',
        place: '计406',
        credit: '4',
        faculty: '计算机工程与科学学院',
        cur_stu_num: 0,
        total_stu_num: 60
      }, {
        course_id: '01001234',
        course_name: '编译原理',
        course_time: '周三1-2',
        teacher_id: '1000',
        teacher_name: '魏晓',
        place: '计406',
        credit: '4',
        faculty: '计算机工程与科学学院',
        cur_stu_num: 0,
        total_stu_num: 60
      }, {
        course_id: '01001234',
        course_name: '编译原理',
        course_time: '周三1-2',
        teacher_id: '1000',
        teacher_name: '魏晓',
        place: '计406'
      }],
      tableStudentGrade: [{
        student_id: '',
        student_name: '',
        routine_score: 0.0,
        exam_score: 0.0,
        total_score: 0.0
      }, {
        student_id: '',
        student_name: '',
        routine_score: 0.0,
        exam_score: 0.0,
        total_score: 0.0
      }]
    }
  },
  methods: {
    handleEdit (index, row) {
      console.log(index)
      this.isShow = true
      this.axios
        .post('http://localhost:8000/search_upload_score')
        .then(resp => {
          if (resp.data.data === 'false') {
            this.$notify({
              title: '还未登分',
              message: '还未登分',
              type: 'error'
            })
          } else {
            this.isShow = true
            let formData = new FormData()
            formData.append('teacher_id', this.tableMyTeachData[index].teacher_id)
            formData.append('course_id', this.tableMyTeachData[index].course_id)
            this.axios
              .post('http://localhost:8000/search_score_by_id', formData)
              .then(resp => {
                console.log('====================start==============')
                console.log(resp)
                if (resp.data.error === 1) {
                  this.$notify({
                    title: '失败',
                    message: resp.data.msg,
                    type: 'error'
                  })
                } else {
                  this.$notify({
                    title: '成功',
                    message: '成功查看成绩',
                    type: 'success'
                  })
                  var list = resp.data.data
                  console.log(this.tableStudentGrade)
                  this.tableStudentGrade.splice(0, this.tableStudentGrade.length)
                  console.log(this.tableStudentGrade)
                  var sumroutinescore = 0
                  var sumexamscore = 0
                  var sumtotalscore = 0
                  var len = 0
                  for (var index in list) {
                    console.log(list[index])
                    this.tableStudentGrade.push({
                      student_id: list[index].student_id,
                      student_name: list[index].student_name,
                      routine_score: list[index].routine_score,
                      exam_score: list[index].exam_score,
                      total_score: list[index].total_score
                    })
                    sumroutinescore += list[index].routine_score
                    sumexamscore += list[index].exam_score
                    sumtotalscore += list[index].total_score
                    len += 1
                  }
                  this.tableStudentGrade.push({
                    student_id: '平均分：',
                    routine_score: sumroutinescore / len,
                    exam_score: sumexamscore / len,
                    total_score: sumtotalscore / len
                  })
                }
              }).catch(err => {
                console.log('请求失败:' + err.status + ',' + err.statusText)
                this.$notify({
                  title: '失败',
                  message: '删除学生信息失败',
                  type: 'error'
                })
              })
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
        })
    }
  },
  created: function () {
    this.isSearch = true
    this.loading = true

    let formData = new FormData()
    formData.append('teacher_id', JSON.parse(localStorage.getItem('userid')))

    this.axios
      .post('http://localhost:8000/search_courseinfo_ownedby', formData)
      .then(resp => {
        var list = resp.data.data
        console.log(this.tableMyTeachData)
        this.tableMyTeachData.splice(0, this.tableMyTeachData.length)
        console.log(this.tableMyTeachData)
        for (var index in list) {
          console.log(list[index])
          this.tableMyTeachData.push({
          //   student_id: list[index].pk,
          //   student_name: list[index].fields.student_name,
          //   sex: list[index].fields.student_sex,
          //   age: list[index].fields.student_age,
          //   faculty: list[index].fields.yxh,
            course_id: list[index].pk,
            course_name: list[index].fields.course_name,
            course_time: list[index].fields.class_time,
            teacher_id: list[index].fields.teacher,
            teacher_name: list[index].fields.teacher_name,
            place: list[index].fields.class_location,
            credit: list[index].fields.credit,
            faculty: list[index].fields.yxh,
            cur_stu_num: list[index].fields.cur_stu_num,
            total_stu_num: list[index].fields.total_stu_num
          })
        }
        this.loading = false
        this.$notify({
          title: '成功',
          message: '查询成功',
          type: 'success'
        })
      }).catch(err => {
        console.log('请求失败:' + err.status + ',' + err.statusText)
        this.$notify({
          title: '失败',
          message: '查询失败',
          type: 'error'
        })
      })
  }
}
</script>

<style scoped>
</style>
