<template>
  <div>
    <div>Admin_Teacher</div>
    <div>
      <el-row>
        <el-button @click="handleSearch" type="primary">查询</el-button>
        <el-button @click="handleAdd" type="info">新增</el-button>
      </el-row>
    </div>
    <el-table v-show="isSearch"
      :data="tableAllTeacherData"
      stripe
      fit
      v-loading="loading"
      style="margin: 0 auto; width: 60%; text-align:center;">
      <el-table-column
        prop="teacher_id"
        label="工号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="teacher_name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="sex"
        label="性别"
        width="180">
      </el-table-column>
      <el-table-column
        prop="age"
        label="年龄"
        width="180">
      </el-table-column>
      <el-table-column
        prop="faculty"
        label="院系"
        width="180">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-form v-show="isAdd" :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="教师号">
        <el-input v-model="ruleForm.teacher_id" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="教师名">
        <el-input v-model="ruleForm.teacher_name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="性别">
        <el-input v-model="ruleForm.teacher_sex" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="院系">
        <el-input v-model="ruleForm.faculty" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="联系方式">
        <el-input v-model="ruleForm.telephone" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="年龄">
        <el-input v-model.number="ruleForm.teacher_age"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
    <el-dialog title="编辑教师信息" :visible.sync="dialogTableVisible">
      <el-form :model="form">
        <el-form-item label="工号" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="form.teacher_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="form.teacher_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="form.teacher_sex" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="年龄" :label-width="formLabelWidth">
          <el-input v-model="form.teacher_age" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="院系" :label-width="formLabelWidth">
          <el-input v-model="form.faculty" autocomplete="off"></el-input>
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
    // var checkAge = (rule, value, callback) => {
    //   if (!value) {
    //     return callback(new Error('年龄不能为空'))
    //   }
    //   setTimeout(() => {
    //     if (!Number.isInteger(value)) {
    //       callback(new Error('请输入数字值'))
    //     } else {
    //       if (value < 18) {
    //         callback(new Error('必须年满18岁'))
    //       } else {
    //         callback()
    //       }
    //     }
    //   }, 1000)
    // }
    // var validatePass = (rule, value, callback) => {
    //   if (value === '') {
    //     callback(new Error('请输入密码'))
    //   } else {
    //     if (this.ruleForm.checkPass !== '') {
    //       this.$refs.ruleForm.validateField('checkPass')
    //     }
    //     callback()
    //   }
    // }
    // var validatePass2 = (rule, value, callback) => {
    //   if (value === '') {
    //     callback(new Error('请再次输入密码'))
    //   } else if (value !== this.ruleForm.pass) {
    //     callback(new Error('两次输入密码不一致!'))
    //   } else {
    //     callback()
    //   }
    // }
    return {
      loading: false,
      isSearch: false,
      isAdd: false,
      dialogTableVisible: false,
      cur_index: '',
      form: {
        teacher_id: '',
        teacher_name: '',
        teacher_sex: '',
        teacher_age: '',
        faculty: ''
      },
      ruleForm: {
        teacher_id: '',
        teacher_name: '',
        teacher_sex: '',
        teacher_age: '',
        faculty: '',
        telephone: ''
      },
      tableAllTeacherData: [{
        teacher_id: '1001',
        teacher_name: '教师姓名',
        sex: '男',
        age: '40',
        faculty: '理学院'
      }, {
        teacher_id: '1001',
        teacher_name: '教师姓名',
        sex: '男',
        age: '40',
        faculty: '理学院'
      }]
      // rules: {
      //   pass: [
      //     { validator: validatePass, trigger: 'blur' }
      //   ],
      //   checkPass: [
      //     { validator: validatePass2, trigger: 'blur' }
      //   ],
      //   age: [
      //     { validator: checkAge, trigger: 'blur' }
      //   ]
      // }
    }
  },
  methods: {
    submitForm (formName) {
      // this.$refs[formName].validate((valid) => {
      //   if (valid) {
      //     alert('submit!')
      //   } else {
      //     console.log('error submit!!')
      //     return false
      //   }
      // })
      console.log('submit')

      let formData = new FormData()
      formData.append('teacher_id', this.ruleForm.teacher_id)
      formData.append('teacher_name', this.ruleForm.teacher_name)
      formData.append('teacher_sex', this.ruleForm.teacher_sex)
      formData.append('teacher_age', this.ruleForm.teacher_age)
      formData.append('faculty', this.ruleForm.faculty)

      this.axios
        .post('http://localhost:8000/insert_teacherinfo', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '新增教师信息失败',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '新增教师信息成功',
              type: 'success'
            })
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '新增教师信息失败',
            type: 'error'
          })
        })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    handleSearch () {
      this.loading = true
      this.axios({
        method: 'get',
        url: 'http://localhost:8000/search_teacherinfo_all'
      }).then(resp => {
        var list = resp.data.data
        console.log(this.tableAllTeacherData)
        this.tableAllTeacherData.splice(0, this.tableAllTeacherData.length)
        console.log(this.tableAllTeacherData)
        for (var index in list) {
          console.log(list[index])
          this.tableAllTeacherData.push({
            teacher_id: list[index].pk,
            teacher_name: list[index].fields.teacher_name,
            sex: list[index].fields.teacher_sex,
            age: list[index].fields.teacher_age,
            faculty: list[index].fields.yxh
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
    handleAdd () {
      this.isAdd = true
      this.isSearch = false
    },
    handleEdit (index, row) {
      this.cur_index = index
      this.dialogTableVisible = true
      this.form.teacher_id = this.tableAllTeacherData[index].teacher_id
      this.form.teacher_name = this.tableAllTeacherData[index].teacher_name
      this.form.teacher_sex = this.tableAllTeacherData[index].sex
      this.form.teacher_age = this.tableAllTeacherData[index].age
      this.form.faculty = this.tableAllTeacherData[index].faculty
    },
    handleDelete (index, row) {
      // alert('delete')
      this.cur_index = index
      let formData = new FormData()
      formData.append('teacher_id', this.tableAllTeacherData[index].teacher_id)

      this.axios
        .post('http://localhost:8000/delete_teacherinfo', formData)
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
              message: '删除教师信息成功',
              type: 'success'
            })
            this.tableAllTeacherData.splice(this.cur_index)
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '删除教师信息失败',
            type: 'error'
          })
        })
    },
    submit () {
      let formData = new FormData()
      formData.append('teacher_id', this.form.teacher_id)
      formData.append('teacher_name', this.form.teacher_name)
      formData.append('teacher_sex', this.form.teacher_sex)
      formData.append('teacher_age', this.form.teacher_age)
      formData.append('faculty', this.form.faculty)

      this.axios
        .post('http://localhost:8000/update_teacherinfo', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '更新教师信息失败',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '更新教师信息成功',
              type: 'success'
            })
            this.dialogTableVisible = false
            this.tableAllTeacherData[this.cur_index].age = this.form.teacher_age
            this.tableAllTeacherData[this.cur_index].faculty = this.form.faculty
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '更新教师信息失败',
            type: 'error'
          })
        })
    }
  }
}
</script>

<style scoped>
</style>
