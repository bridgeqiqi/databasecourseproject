<template>
  <div>
    <div>Teacher_SearchCourse</div>
    <el-button @click="handleSearch" type="primary" round style="margin: 0 auto; width: 15%; text-align:center">查询</el-button>
    <el-table v-show="isSearch"
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
            type="primary"
            @click="handleEdit(scope.$index, scope.row)">查看详情</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-table v-show="isSearch_s"
      :data="tableAllStudentData"
      v-loading="sloading"
      stripe
      fit
      style="margin: 0 auto; width: 50%; text-align:center;">
      <el-table-column
        prop="student_id"
        label="学号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="student_name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="student_sex"
        label="性别"
        width="180">
      </el-table-column>
      <el-table-column
        prop="student_age"
        label="年龄"
        width="180">
      </el-table-column>
      <el-table-column
        prop="faculty"
        label="院系"
        width="180">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isSearch: false,
      isSearch_s: false,
      loading: false,
      sloading: false,
      tableAllStudentData: [{
        student_id: '16122435',
        student_name: '高佳琪',
        student_sex: '男',
        student_age: '20',
        faculty: '计算机工程与科学学院'
      }],
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
      }]
    }
  },
  methods: {
    handleSearch () {
      this.isSearch = true
      this.loading = true
      this.isSearch_s = false

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
    },
    handleEdit (index, row) {
      console.log(index)
      this.isSearch_s = true
      this.sloading = true
      let formData = new FormData()
      formData.append('teacher_id', this.tableMyTeachData[index].teacher_id)
      formData.append('course_id', this.tableMyTeachData[index].course_id)
      this.axios
        .post('http://localhost:8000/search_studentinfo_by_id', formData)
        .then(resp => {
          // console.log("====================start==============")
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
              message: '查看成功',
              type: 'success'
            })
            var list = resp.data.data
            console.log(this.tableAllStudentData)
            this.tableAllStudentData.splice(0, this.tableAllStudentData.length)
            console.log(this.tableAllStudentData)
            for (var index in list) {
              console.log(list[index])
              this.tableAllStudentData.push({
                student_id: list[index].student_id,
                student_name: list[index].student_name,
                student_sex: list[index].student_sex,
                student_age: list[index].student_age,
                faculty: list[index].faculty
              })
            }
            this.sloading = false
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
  }
}
</script>

<style scoped>
</style>
