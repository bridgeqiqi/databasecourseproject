<template>
  <div>
    <div>Admin_Student</div>
    <div>
      <el-row>
        <el-button @click="handleSearch" type="primary">查询</el-button>
        <el-button @click="handleAdd" type="info">新增</el-button>
      </el-row>
    </div>
    <el-table v-show="isSearch"
      :data="tableAllStudentData"
      v-loading="loading"
      stripe
      fit
      style="margin: 0 auto; width: 60%; text-align:center;">
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
      <el-form-item label="学号" prop="pass">
        <el-input v-model="ruleForm.student_id" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="姓名" prop="pass">
        <el-input v-model="ruleForm.student_name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="pass">
        <el-input v-model="ruleForm.student_sex" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="院系" prop="pass">
        <el-input v-model="ruleForm.faculty" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="联系方式" prop="pass">
        <el-input v-model="ruleForm.telephone" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="年龄" prop="age">
        <el-input v-model="ruleForm.student_age"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
    <el-dialog title="编辑学生信息" :visible.sync="dialogTableVisible">
      <el-form :model="form">
        <el-form-item label="学号" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="form.student_id" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="form.student_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" :label-width="formLabelWidth">
          <el-input :disabled="true" v-model="form.student_sex" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="年龄" :label-width="formLabelWidth">
          <el-input v-model="form.student_age" autocomplete="off"></el-input>
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
      isSearch: false,
      isAdd: false,
      loading: false,
      dialogTableVisible: false,
      cur_index: '',
      form: {
        student_id: '',
        student_name: '',
        student_sex: '',
        student_age: '',
        faculty: ''
      },
      tableAllStudentData: [{
        student_id: '16122435',
        student_name: '高佳琪',
        sex: '男',
        age: '20',
        faculty: '计算机工程与科学学院'
      }, {
        student_id: '16122435',
        student_name: '高佳琪',
        sex: '男',
        age: '20',
        faculty: '计算机工程与科学学院'
      }],
      ruleForm: {
        student_id: '',
        student_name: '',
        student_sex: '',
        student_age: '',
        faculty: ''
      }
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
      let formData = new FormData()
      formData.append('student_id', this.ruleForm.student_id)
      formData.append('student_name', this.ruleForm.student_name)
      formData.append('student_sex', this.ruleForm.student_sex)
      formData.append('student_age', this.ruleForm.student_age)
      formData.append('faculty', this.ruleForm.faculty)

      this.axios
        .post('http://localhost:8000/insert_studentinfo', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '新增学生信息失败',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '新增学生信息成功',
              type: 'success'
            })
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '新增学生信息失败',
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
        url: 'http://localhost:8000/search_studentinfo_all'
      }).then(resp => {
        var list = resp.data.data
        console.log(this.tableAllStudentData)
        this.tableAllStudentData.splice(0, this.tableAllStudentData.length)
        console.log(this.tableAllStudentData)
        for (var index in list) {
          console.log(list[index])
          this.tableAllStudentData.push({
            student_id: list[index].pk,
            student_name: list[index].fields.student_name,
            sex: list[index].fields.student_sex,
            age: list[index].fields.student_age,
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
      this.form.student_id = this.tableAllStudentData[index].student_id
      this.form.student_name = this.tableAllStudentData[index].student_name
      this.form.student_sex = this.tableAllStudentData[index].sex
      this.form.student_age = this.tableAllStudentData[index].age
      this.form.faculty = this.tableAllStudentData[index].faculty
    },
    handleDelete (index, row) {
      // alert('delete')
      this.cur_index = index
      let formData = new FormData()
      formData.append('student_id', this.tableAllStudentData[index].student_id)

      this.axios
        .post('http://localhost:8000/delete_studentinfo', formData)
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
              message: '删除学生信息成功',
              type: 'success'
            })
            this.tableAllStudentData.splice(this.cur_index)
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '删除学生信息失败',
            type: 'error'
          })
        })
    },
    submit () {
      let formData = new FormData()
      formData.append('student_id', this.form.student_id)
      formData.append('student_name', this.form.student_name)
      formData.append('student_sex', this.form.student_sex)
      formData.append('student_age', this.form.student_age)
      formData.append('faculty', this.form.faculty)

      this.axios
        .post('http://localhost:8000/update_studentinfo', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '更新学生信息失败',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '更新学生信息成功',
              type: 'success'
            })
            this.dialogTableVisible = false
            this.tableAllStudentData[this.cur_index].age = this.form.student_age
            this.tableAllStudentData[this.cur_index].faculty = this.form.faculty
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '更新学生信息失败',
            type: 'error'
          })
        })
    }
  }
}
</script>

<style scoped>
</style>
