<template>
  <div>
    <div>Admin_Course</div>
    <div>
      <el-row>
        <el-button @click="handleSearch" type="primary">查询</el-button>
        <el-button @click="handleAdd" type="info">新增</el-button>
      </el-row>
    </div>
    <el-table v-show="isSearch"
      :data="tableAllCourseData"
      v-loading="loading"
      stripe
      fit
      style="margin: 0 auto; width: 95%; text-align:center;">
      <el-table-column
        prop="course_id"
        label="课程号"
        width="150">
      </el-table-column>
      <el-table-column
        prop="course_name"
        label="课程名"
        width="150">
      </el-table-column>
      <el-table-column
        prop="credit"
        label="学分"
        width="150">
      </el-table-column>
      <el-table-column
        prop="course_time"
        label="上课时间"
        width="180">
      </el-table-column>
      <el-table-column
        prop="teacher_id"
        label="教师号"
        width="150">
      </el-table-column>
      <el-table-column
        prop="teacher_name"
        label="教师名"
        width="150">
      </el-table-column>
      <el-table-column
        prop="place"
        label="上课教室"
        width="150">
      </el-table-column>
      <el-table-column
        prop="faculty"
        label="开课学院院系号"
        width="150">
      </el-table-column>
      <el-table-column
        prop="cur_stu_num"
        label="当前选课人数"
        width="150">
      </el-table-column>
      <el-table-column
        prop="total_stu_num"
        label="最大选课人数"
        width="150">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">不开</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-form ref="form" :model="form" label-width="100px" v-show="isAdd" style="margin: 0 auto; width: 50%">
      <el-form-item label="课程号">
        <el-input v-model="form.course_id"></el-input>
      </el-form-item>
      <el-form-item label="课程名">
        <el-input v-model="form.course_name"></el-input>
      </el-form-item>
      <el-form-item label="教师号">
        <el-input v-model="form.teacher_id"></el-input>
      </el-form-item>
      <el-form-item label="教师姓名">
        <el-input v-model="form.teacher_name"></el-input>
      </el-form-item>
      <el-form-item label="上课教室">
        <el-input v-model="form.place"></el-input>
      </el-form-item>
      <el-form-item label="开课人数">
        <el-input v-model="form.total_stu_num"></el-input>
      </el-form-item>
      <el-form-item label="学分">
        <el-input v-model="form.credit"></el-input>
      </el-form-item>
      <el-form-item label="上课时间">
        <el-input v-model="dynamicValidateForm.class_time"></el-input>
      </el-form-item>
      <el-form-item
        v-for="(domain, index) in dynamicValidateForm.domains"
        :label="'上课时间' + (index+1)"
        :key="domain.key"
        :prop="'domains.' + index + '.value'"
      >
        <el-input v-model="domain.value"></el-input><el-button @click.prevent="removeDomain(domain)">删除</el-button>
      </el-form-item>
      <el-form-item>
        <el-button @click="addDomain">新增上课时间</el-button>
        <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
      </el-form-item>
      <el-button type="primary" @click="submitForm('dynamicValidateForm')">确认提交</el-button>
    </el-form>
    <el-dialog title="编辑课程信息" :visible.sync="dialogTableVisible">
      <el-form :model="dialogueform">
        <el-form-item label="课程号" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="dialogueform.course_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="课程名" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="dialogueform.course_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="学分" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="dialogueform.credit" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="教师号" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="dialogueform.teacher_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="教师姓名" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="dialogueform.teacher_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="上课时间" :label-width="formLabelWidth">
          <el-input v-model="dialogueform.class_time" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="上课地点" :label-width="formLabelWidth">
          <el-input v-model="dialogueform.class_location" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="最大选课人数" :label-width="formLabelWidth">
          <el-input v-model="dialogueform.total_stu_num" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogTableVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit()">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      loading: false,
      isSearch: false,
      isAdd: false,
      dialogTableVisible: false,
      cur_index: '',
      dialogueform: {
        course_id: '',
        course_name: '',
        credit: '',
        teacher_id: '',
        teacher_name: '',
        class_time: '',
        class_location: '',
        total_stu_num: ''
      },
      dynamicValidateForm: {
        domains: [{
          value: ''
        }],
        class_time: ''
      },
      form: {
        course_id: '',
        course_name: '',
        teacher_id: '',
        teacher_name: '',
        place: '',
        credit: '',
        total_stu_num: ''
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
      }]
    }
  },
  methods: {
    handleSearch: function () {
      this.loading = true
      this.axios({
        method: 'get',
        url: 'http://localhost:8000/search_courseinfo_all'
      }).then(resp => {
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
        // console.log(list)
      }).catch(err => {
        console.log('请求失败:' + err.status + ',' + err.statusText)
      })
      this.isSearch = true
      this.isAdd = false
    },
    handleAdd: function () {
      this.isAdd = true
      this.isSearch = false
    },
    submitForm (formName) {
      // this.$refs[formName].validate((valid) => {
      //   if (valid) {
      //     alert('submit!')
      //   } else {
      //     console.log('error submit!!')
      //     return false
      //   }
      // })
      console.log(this.dynamicValidateForm.class_time)
      var classtime = this.dynamicValidateForm.class_time
      for (var index in this.dynamicValidateForm.domains) {
        classtime = classtime + ' ' + this.dynamicValidateForm.domains[index].value
      }
      console.log(classtime)
      console.log('submit')

      let formData = new FormData()
      formData.append('course_id', this.form.course_id)
      formData.append('course_name', this.form.course_name)
      formData.append('teacher_id', this.form.teacher_id)
      formData.append('teacher_name', this.form.teacher_name)
      formData.append('class_location', this.form.place)
      formData.append('total_stu_num', this.form.total_stu_num)
      formData.append('credit', this.form.credit)
      formData.append('class_time', classtime)

      this.axios
        .post('http://localhost:8000/insert_courseinfo', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '新增课程信息失败',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '新增课程信息成功',
              type: 'success'
            })
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '新增课程信息失败',
            type: 'error'
          })
        })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    removeDomain (item) {
      var index = this.dynamicValidateForm.domains.indexOf(item)
      if (index !== -1) {
        this.dynamicValidateForm.domains.splice(index, 1)
      }
    },
    addDomain () {
      this.dynamicValidateForm.domains.push({
        value: '',
        key: Date.now()
      })
    },
    handleEdit (index, row) {
      this.cur_index = index
      this.dialogTableVisible = true
      this.dialogueform.course_id = this.tableAllCourseData[index].course_id
      this.dialogueform.course_name = this.tableAllCourseData[index].course_name
      this.dialogueform.credit = this.tableAllCourseData[index].credit
      this.dialogueform.teacher_id = this.tableAllCourseData[index].teacher_id
      this.dialogueform.teacher_name = this.tableAllCourseData[index].teacher_name
      this.dialogueform.class_time = this.tableAllCourseData[index].course_time
      this.dialogueform.class_location = this.tableAllCourseData[index].place
      this.dialogueform.total_stu_num = this.tableAllCourseData[index].total_stu_num
    },
    handleDelete (index, row) {
      // alert('delete')
      this.cur_index = index
      let formData = new FormData()
      formData.append('course_id', this.tableAllCourseData[index].course_id)
      formData.append('teacher_id', this.tableAllCourseData[index].teacher_id)
      this.axios
        .post('http://localhost:8000/delete_courseinfo', formData)
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
              message: '删除课程信息成功',
              type: 'success'
            })
            this.tableAllCourseData[this.cur_index].class_time = '不开'
            this.tableAllCourseData[this.cur_index].cur_stu_num = 0
            this.tableAllCourseData[this.cur_index].total_stu_num = 0
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '删除课程信息失败',
            type: 'error'
          })
        })
    },
    submit () {
      let formData = new FormData()
      // this.dialogueform.course_id = this.tableAllCourseData[index].course_id
      // this.dialogueform.course_name = this.tableAllCourseData[index].course_name
      // this.dialogueform.credit = this.tableAllCourseData[index].credit
      // this.dialogueform.teacher_id = this.tableAllCourseData[index].teacher_id
      // this.dialogueform.teacher_name = this.tableAllCourseData[index].teacher_name
      // this.dialogueform.class_time = this.tableAllCourseData[index].course_time
      // this.dialogueform.class_location = this.tableAllCourseData[index].place
      // this.dialogueform.total_stu_num = this.tableAllCourseData[index].total_stu_num
      formData.append('course_id', this.dialogueform.course_id)
      formData.append('course_name', this.dialogueform.course_name)
      formData.append('credit', this.dialogueform.credit)
      formData.append('teacher_id', this.dialogueform.teacher_id)
      formData.append('teacher_name', this.dialogueform.teacher_name)
      formData.append('class_time', this.dialogueform.class_time)
      formData.append('class_location', this.dialogueform.class_location)
      formData.append('total_stu_num', this.dialogueform.total_stu_num)

      this.axios
        .post('http://localhost:8000/update_courseinfo', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '更新课程信息失败',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '更新课程信息成功',
              type: 'success'
            })
            this.dialogTableVisible = false
            this.tableAllCourseData[this.cur_index].course_time = this.dialogueform.class_time
            this.tableAllCourseData[this.cur_index].place = this.dialogueform.class_location
            this.tableAllCourseData[this.cur_index].total_stu_num = this.dialogueform.total_stu_num
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '更新课程信息失败',
            type: 'error'
          })
        })
    }
  }
}
</script>

<style scoped>
</style>
