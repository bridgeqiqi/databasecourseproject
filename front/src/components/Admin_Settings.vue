<template>
  <div>
  <div>Admin_Settings</div>
  <div style="margin: 0 auto; width: 30vw">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="开放选课">
        <el-switch
          v-model="form.chooseClass"
          active-text="开放"
          inactive-text="关闭"
          @change="changeChooseClass">
        </el-switch>
      </el-form-item>
      <el-form-item label="开放登分">
        <el-switch
          v-model="form.uploadScore"
          active-text="开放"
          inactive-text="关闭"
          @change="changeUploadScore">
        </el-switch>
      </el-form-item>
    </el-form>
  </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      form: {
        chooseClass: false,
        uploadScore: false
      }
    }
  },
  methods: {
    changeChooseClass: function () {
      console.log(this.form.chooseClass)
      var url = ''
      let formData = new FormData()
      if (this.form.chooseClass === false) {
        url = 'http://localhost:8000/stop_choose_course'
      } else {
        url = 'http://localhost:8000/start_choose_course'
      }
      this.axios
        .post(url, formData)
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
              message: resp.data.msg,
              type: 'success'
            })
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '失败',
            type: 'error'
          })
        })
    },
    changeUploadScore: function () {
      console.log(this.form.uploadScore)
      var url = ''
      let formData = new FormData()
      if (this.form.uploadScore === false) {
        url = 'http://localhost:8000/stop_upload_score'
      } else {
        url = 'http://localhost:8000/start_upload_score'
      }
      this.axios
        .post(url, formData)
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
              message: resp.data.msg,
              type: 'success'
            })
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '失败',
            type: 'error'
          })
        })
    }
  },
  created: function () {
    let formData = new FormData()
    this.axios
      .post('http://localhost:8000/search_two_states', formData)
      .then(resp => {
        console.log(resp)
        console.log(this.form.chooseClass)
        console.log(this.form.uploadScore)
        this.form.chooseClass = resp.data.is_choose_course
        this.form.uploadScore = resp.data.is_upload_score
        console.log(this.form.chooseClass)
        console.log(this.form.uploadScore)
      }).catch(err => {
        console.log('请求失败:' + err.status + ',' + err.statusText)
        this.$notify({
          title: '失败',
          message: '失败',
          type: 'error'
        })
      })
  }
}
</script>

<style scoped>
</style>
