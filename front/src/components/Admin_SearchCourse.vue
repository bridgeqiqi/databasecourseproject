<template>
  <div>
    <div>Admin_SearchCourse</div>
    <el-form ref="form" :model="form" status-icon label-width="100px">
      <el-form-item label="课程号">
        <el-input v-model="form.course_id"></el-input>
      </el-form-item>
      <el-form-item label="教师号">
        <el-input v-model="form.teacher_id"></el-input>
      </el-form-item>
    </el-form>
    <el-button @click="handleSearch()" type="primary" round style="margin: 0 auto; width: 15%; text-align:center;">查询</el-button>
    <div>下面放图表 和 统计信息</div>
    <el-table v-show="isSearch"
      :data="tableAllScoreData"
      v-loading="loading"
      stripe
      fit
      style="margin: 0 auto; width: 60%; text-align:center;">
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
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isSearch: false,
      loading: false,
      form: {
        course_id: '',
        teacher_id: ''
      },
      tableAllScoreData: [{
        student_id: '',
        student_name: '',
        routine_score: '',
        exam_score: '',
        total_score: ''
      }]
    }
  },
  methods: {
    handleSearch () {
      console.log('search')
      let formData = new FormData()
      formData.append('course_id', this.form.course_id)
      formData.append('teacher_id', this.form.teacher_id)

      this.axios
        .post('http://localhost:8000/search_score_by_id', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: '查询课程成绩失败',
              type: 'error'
            })
          } else {
            this.$notify({
              title: '成功',
              message: '查询课程成绩成功',
              type: 'success'
            })
            this.isSearch = true
            var list = resp.data.data
            console.log(this.tableAllScoreData)
            this.tableAllScoreData.splice(0, this.tableAllScoreData.length)
            console.log(this.tableAllScoreData)
            var sumroutine = 0
            var sumexam = 0
            var sumtotal = 0
            for (var index in list) {
              console.log(list[index])
              this.tableAllScoreData.push({
                student_id: list[index].student_id,
                student_name: list[index].student_name,
                routine_score: list[index].routine_score,
                exam_score: list[index].exam_score,
                total_score: list[index].total_score
              })
              sumroutine = parseFloat(sumroutine) + parseFloat(list[index].routine_score)
              sumexam = parseFloat(sumexam) + parseFloat(list[index].exam_score)
              sumtotal = parseFloat(sumtotal) + parseFloat(list[index].total_score)
            }
            var len = this.tableAllScoreData.length
            if (len !== 0) {
              this.tableAllScoreData.push({
                student_id: '平均分',
                routine_score: (sumroutine / len).toFixed(2),
                exam_score: (sumexam / len).toFixed(2),
                total_score: (sumtotal / len).toFixed(2)
              })
            }
          }
        }).catch(err => {
          console.log('请求失败:' + err.status + ',' + err.statusText)
          this.$notify({
            title: '失败',
            message: '查询课程成绩失败',
            type: 'error'
          })
        })
    }
  }
}
</script>

<style scoped>
</style>
