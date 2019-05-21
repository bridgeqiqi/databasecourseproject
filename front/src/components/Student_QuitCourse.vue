<template>
  <div>
    <div>Student_QuitCourse</div>
    <el-table v-show="isSearch"
      :data="tableAllCourseData"
      stripe
      fit
      style="margin: 0 auto; width: 90%; text-align:center;">
      <el-table-column prop="course_id" label="课程号" width="150">
      </el-table-column>
      <el-table-column prop="course_name" label="课程名" width="150">
      </el-table-column>
      <el-table-column prop="credit" label="学分" width="150">
      </el-table-column>
      <el-table-column prop="course_time" label="上课时间" width="150">
      </el-table-column>
      <el-table-column prop="teacher_id" label="教师号" width="150">
      </el-table-column>
      <el-table-column prop="teacher_name" label="教师名" width="150">
      </el-table-column>
      <el-table-column prop="place" label="上课教室" width="150">
      </el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            @click="handleEdit(scope.$index, scope.row)">退课</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isSearch: true,
      tableAllCourseData: [{
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
      }, {
        course_id: '01001234',
        course_name: '编译原理',
        course_time: '周三1-2',
        teacher_id: '1000',
        teacher_name: '魏晓',
        place: '计406'
      }, {
        course_id: '01001234',
        course_name: '编译原理',
        course_time: '周三1-2',
        teacher_id: '1000',
        teacher_name: '魏晓',
        place: '计406'
      }]
    }
  },
  methods: {
    handleEdit (index, row) {
      alert('确定要退这门课吗?' + row.course_id + ' ' + row.course_name)
      let formData = new FormData()
      formData.append('student_id', JSON.parse(localStorage.getItem('userid')))
      formData.append('teacher_id', row.teacher_id)
      formData.append('course_id', row.course_id)
      this.axios
        .post('http://localhost:8000/quit_course', formData)
        .then(resp => {
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
              message: '退课成功',
              type: 'success'
            })
            this.tableAllCourseData.splice(index)
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '退课失败',
            type: 'error'
          })
        })
    }
  },
  created: function () {
    let formData = new FormData()
    formData.append('student_id', JSON.parse(localStorage.getItem('userid')))
    this.axios
      .post('http://localhost:8000/search_my_course', formData)
      .then(resp => {
        console.log(resp)
        if (resp.data.error === 1) {
          this.$notify({
            title: '失败',
            message: '查找失败',
            type: 'error'
          })
        } else {
          var list = resp.data.data
          console.log(this.tableAllCourseData)
          this.tableAllCourseData.splice(0, this.tableAllCourseData.length)
          console.log(this.tableAllCourseData)
          for (var index in list) {
            console.log(list[index])
            this.tableAllCourseData.push({
            //   student_id: list[index].pk,
            //   student_name: list[index].fields.student_name,
            //   sex: list[index].fields.student_sex,
            //   age: list[index].fields.student_age,
            //   faculty: list[index].fields.yxh,
              course_id: list[index].course_id,
              course_name: list[index].course_name,
              course_time: list[index].class_time,
              teacher_id: list[index].teacher_id,
              teacher_name: list[index].teacher_name,
              place: list[index].class_location,
              credit: list[index].credit
            })
          }
          this.$notify({
            title: '成功',
            message: '查询成功',
            type: 'success'
          })
        }
      }).catch(err => {
        console.log('请求失败:' + err.status + ',' + err.statusText)
        this.$notify({
          title: '失败',
          message: '查找失败',
          type: 'error'
        })
      })
  }
}
</script>

<style scoped>
</style>
