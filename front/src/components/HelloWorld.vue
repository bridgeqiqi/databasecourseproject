<template>
  <div class="hello">
    <img src="../assets/logo.png">
    <h1>{{ msg_english }}</h1>
    <h1>{{ msg_chinese }}</h1>
    <h1><br/></h1>

    <div class="inputmargin">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="用户名：">
          <el-input
            v-model="form.username"
            placeholder="请输入用户名"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="密码：">
          <el-input
            v-model="form.password"
            placeholder="请输入密码"
            show-password
            clearable
          ></el-input>
        </el-form-item>
        <div>
          <el-button
            type="primary"
            @click="To('/Student')"
            route="/student"
          >登录</el-button>
          <el-button>注册</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import AppVue from '../App.vue'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg_english: 'Welcome to Educational Administration Management System from Shanghai University',
      msg_chinese: '欢迎来到上海大学教务管理系统',
      inputValue: '',
      list: [],
      form: {
        username: '',
        password: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      }
    }
  },
  created: function () {
    localStorage.setItem('isTeacher', false)
    localStorage.setItem('isAdmin', false)
    localStorage.setItem('isStudent', false)
  },
  methods: {
    To: function (url) {
      let formData = new FormData()
      formData.append('username', this.form.username)
      formData.append('password', this.form.password)
      this.axios
        .post('http://localhost:8000/check_login', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '用户名不存在或密码错误',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '登录成功',
              type: 'success'
            })
            if (resp.data.identifier === '学生') {
              localStorage.setItem('isTeacher', false)
              localStorage.setItem('isAdmin', false)
              localStorage.setItem('isStudent', true)
              localStorage.setItem('userid', this.form.username)
              this.$router.push({path: '/App', components: AppVue})
            } else if (resp.data.identifier === '教师') {
              localStorage.setItem('isTeacher', true)
              localStorage.setItem('isAdmin', false)
              localStorage.setItem('isStudent', false)
              localStorage.setItem('userid', this.form.username)
              this.$router.push({path: '/App', components: AppVue})
            } else if (resp.data.identifier === '管理员') {
              localStorage.setItem('isTeacher', false)
              localStorage.setItem('isAdmin', true)
              localStorage.setItem('isStudent', false)
              localStorage.setItem('userid', this.form.username)
              this.$router.push({path: '/App', components: AppVue})
            }
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '网络异常',
            type: 'error'
          })
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.inputmargin {
  margin: 0 auto;
  width: 30vw;
}

/* .buttonWrapper {
  margin: 0 auto;
  width: 200px;
} */
</style>
