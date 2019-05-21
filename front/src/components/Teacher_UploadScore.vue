<template>
  <div>
    <div>Teacher_UploadScore</div>
    <div>请选择以下一门课程</div>
    <el-table
      :data="tableMyTeachData"
      v-loading="loading"
      stripe
      fit
      style="margin: 0 auto; width: 95%; text-align:center;">
      <el-table-column prop="course_id" label="课程号" width="180">
      </el-table-column>
      <el-table-column prop="course_name" label="课程名" width="180">
      </el-table-column>
      <el-table-column prop="credit" label="学分" width="180">
      </el-table-column>
      <el-table-column prop="course_time" label="上课时间" width="180">
      </el-table-column>
      <el-table-column prop="teacher_id" label="教师号" width="180">
      </el-table-column>
      <el-table-column prop="teacher_name" label="教师名" width="180">
      </el-table-column>
      <el-table-column prop="place" label="上课教室" width="180">
      </el-table-column>
      <el-table-column prop="cur_stu_num" label="当前选课人数" width="180">
      </el-table-column>
      <el-table-column prop="total_stu_num" label="最大选课人数" width="180">
      </el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="success"
            @click="handleEdit(scope.$index, scope.row)">上传成绩录入分数</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-table
      v-show="isShow"
      :data="tableStudentGrade"
      stripe
      fit
      style="margin: 0 auto; width: 56%; text-align:center;">
      <el-table-column prop="student_id" label="学号" width="180">
      </el-table-column>
      <el-table-column prop="student_name" label="姓名" width="180">
      </el-table-column>
      <el-table-column prop="routine_score" label="平时成绩" width="180">
      </el-table-column>
      <el-table-column prop="exam_score" label="考试成绩" width="180">
      </el-table-column>
      <el-table-column prop="total_score" label="总评成绩" width="180">
      </el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="success"
            @click="handleUploadScore(scope.$index, scope.row)">编辑登分</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title="编辑登分" :visible.sync="dialogTableVisible">
      <el-form :model="form">
        <el-form-item label="学号" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="form.student_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="form.student_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="平时成绩" :label-width="formLabelWidth">
          <el-input v-model="form.pingshi_score" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="考试成绩" :label-width="formLabelWidth">
          <el-input v-model="form.exam_score" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogTableVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit()">确 定</el-button>
      </div>
    </el-dialog>
    <el-button v-show="isShow" type="primary" style="margin: 0 auto; width: 15%; text-align:center;">确认提交</el-button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isShow: false,
      formLabelWidth: '120px',
      dialogTableVisible: false,
      cur_student_row_index: 0,
      cur_course_id: '',
      form: {
        student_id: '',
        student_name: '',
        pingshi_score: '',
        exam_score: ''
      },
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
    handleUploadScore (index, row) {
      this.dialogTableVisible = true
      this.form.student_id = this.tableStudentGrade[index].student_id
      this.form.student_name = this.tableStudentGrade[index].student_name
      this.form.pingshi_score = this.tableStudentGrade[index].routine_score
      this.form.exam_score = this.tableStudentGrade[index].exam_score
    },
    submit () {
      console.log(this.form.pingshi_score)
      console.log(this.form.exam_score)
      this.tableStudentGrade[this.cur_student_row_index].routine_score = this.form.pingshi_score
      this.tableStudentGrade[this.cur_student_row_index].exam_score = this.form.exam_score
      this.tableStudentGrade[this.cur_student_row_index].total_score = (parseFloat(this.form.exam_score) + parseFloat(this.form.pingshi_score)) / 2
      this.dialogTableVisible = false

      let formData = new FormData()
      formData.append('student_id', this.form.student_id)
      formData.append('course_id', this.cur_course_id)
      formData.append('teacher_id', JSON.parse(localStorage.getItem('userid')))
      formData.append('routine_score', this.form.pingshi_score)
      formData.append('exam_score', this.form.exam_score)

      this.axios
        .post('http://localhost:8000/upload_grade', formData)
        .then(resp => {
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '录入成绩失败',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '录入成功',
              type: 'success'
            })
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '录入成绩失败',
            type: 'error'
          })
        })
    },
    handleEdit (index, row) {
      this.cur_student_row_index = index
      this.cur_course_id = row.course_id
      this.axios
        .post('http://localhost:8000/search_upload_score')
        .then(resp => {
          if (resp.data.data === 'false') {
            this.$notify({
              title: '未到时间',
              message: '还未能上传成绩',
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
                    message: '准备上传成绩',
                    type: 'success'
                  })
                  var list = resp.data.data
                  console.log(this.tableStudentGrade)
                  this.tableStudentGrade.splice(0, this.tableStudentGrade.length)
                  console.log(this.tableStudentGrade)
                  for (var index in list) {
                    console.log(list[index])
                    this.tableStudentGrade.push({
                      student_id: list[index].student_id,
                      student_name: list[index].student_name,
                      routine_score: list[index].routine_score,
                      exam_score: list[index].exam_score,
                      total_score: list[index].total_score
                    })
                  }
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
