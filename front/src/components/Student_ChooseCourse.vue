<template>
  <div>
    <div>Student_ChooseCourse</div>
    <el-form ref="form" :model="form" status-icon label-width="100px">
      <el-form-item label="课程号">
        <el-input v-model="form.course_id"></el-input>
      </el-form-item>
      <el-form-item label="课程名">
        <el-input v-model="form.course_name"></el-input>
      </el-form-item>
      <el-form-item label="上课时间">
        <el-input v-model="form.class_time"></el-input>
      </el-form-item>
      <el-form-item label="教师号">
        <el-input v-model="form.teacher_id"></el-input>
      </el-form-item>
      <el-form-item label="教师名">
        <el-input v-model="form.teacher_name"></el-input>
      </el-form-item>
    </el-form>
    <el-button @click="handleSearch" type="primary" round style="margin: 0 auto; width: 15%; text-align:center;">查询</el-button>
    <el-table v-show="isSearch"
      :data="tableAllCourseData"
      stripe
      fit
      style="margin: 0 auto; width: 95%; text-align:center;">
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
      <el-table-column prop="faculty" label="开课学院院系号" width="150">
      </el-table-column>
      <el-table-column prop="cur_stu_num" label="当前选课人数" width="150">
      </el-table-column>
      <el-table-column prop="total_stu_num" label="最大选课人数" width="150">
      </el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="success"
            @click="handleEdit(scope.$index, scope.row)">选课</el-button>
        </template>
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isSearch: false,
      form: {
        course_id: '',
        course_name: '',
        class_time: '',
        teacher_id: '',
        teacher_name: ''
      },
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
    handleSearch () {
      let formData = new FormData()
      this.axios
        .post('http://localhost:8000/search_choose_course', formData)
        .then(resp => {
          if (resp.data.data === 'true') {
            this.isSearch = true
            let formData = new FormData()
            formData.append('course_id', this.form.course_id)
            formData.append('course_name', this.form.course_name)
            formData.append('class_time', this.form.course_id)
            formData.append('teacher_id', this.form.teacher_id)
            formData.append('teacher_name', this.form.teacher_name)
            this.axios
              .post('http://localhost:8000/search_courseinfo_by', formData)
              .then(resp => {
                console.log(resp)
                console.log(resp.data)
                var list = resp.data.data
                console.log(this.tableAllCourseData)
                this.tableAllCourseData.splice(0, this.tableAllCourseData.length)
                console.log(this.tableAllCourseData)
                console.log('----------------------------')
                console.log(list)
                for (var index in list) {
                  console.log(list[index])
                  this.tableAllCourseData.push({
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
                this.$notify({
                  title: '成功',
                  message: '查询成功',
                  type: 'success'
                })
                // console.log(list)
              }).catch(err => {
                console.log('请求失败:' + err.status + ',' + err.statusText)
              })
          } else {
            this.$notify({
              title: '失败',
              message: '选课时间未到',
              type: 'error'
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
      alert(row.course_name)
      if (row.course_time === '不开') {
        this.$notify({
          title: '失败',
          message: '课程不开，选课失败',
          type: 'error'
        })
      } else if (row.cur_stu_num === row.total_stu_num) {
        this.$notify({
          title: '失败',
          message: '选课失败,人数限制',
          type: 'error'
        })
      } else {
        let formData = new FormData()
        formData.append('course_id', row.course_id)
        formData.append('student_id', JSON.parse(localStorage.getItem('userid')))
        formData.append('teacher_id', row.teacher_id)
        formData.append('class_time', row.course_time)
        this.axios
          .post('http://localhost:8000/choose_course', formData)
          .then(resp => {
            console.log(resp)
            if (resp.data.error === 1) {
              this.$notify({
                title: '失败',
                message: '选课失败',
                type: 'error'
              })
            } else {
              this.$notify({
                title: '成功',
                message: '选课成功',
                type: 'success'
              })
            }
          }).catch(err => {
            console.log('请求失败:' + err.status + ',' + err.statusText)
            this.$notify({
              title: '失败',
              message: '选课失败',
              type: 'error'
            })
          })
      }
    }
  }
}
</script>

<style scoped>
</style>
