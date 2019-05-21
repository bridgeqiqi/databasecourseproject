<template>
  <div>
    <div>Student_MyScore</div>
    <div>下面是统计信息</div>
    <el-button type="primary" @click="handleSearch">查询</el-button>
    <el-table v-show="isSearch"
      :data="tableMyScore"
      stripe
      fit
      style="margin: 0 auto; width: 90%; text-align:center;">
      <el-table-column prop="course_id" label="课程号" width="150">
      </el-table-column>
      <el-table-column prop="course_name" label="课程名" width="150">
      </el-table-column>
      <el-table-column prop="teacher_id" label="教师号" width="150">
      </el-table-column>
      <el-table-column prop="teacher_name" label="教师名" width="150">
      </el-table-column>
      <el-table-column prop="credit" label="学分" width="150">
      </el-table-column>
      <el-table-column prop="score" label="总评成绩" width="150">
      </el-table-column>
      <el-table-column prop="gpa" label="绩点" width="150">
      </el-table-column>
    </el-table>
    <div v-show="isSearch">学分: {{sum_credits}} 平均绩点: {{average_gpa}}</div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isSearch: false,
      sum_credits: 0,
      average_gpa: 0.0,
      tableMyScore: [{
        course_id: '01001234',
        course_name: '编译原理',
        teacher_id: '1000',
        teacher_name: '魏晓',
        credit: 4,
        score: 95,
        gpa: 4.0.toFixed(1)
      }, {
        course_id: '01004567',
        course_name: '计算机系统结构',
        teacher_id: '1000',
        teacher_name: '雷咏梅',
        credit: 4,
        score: 95,
        gpa: 4.0.toFixed(1)
      }]
    }
  },
  methods: {
    handleSearch () {
      let formData = new FormData()
      formData.append('student_id', JSON.parse(localStorage.getItem('userid')))
      this.axios
        .post('http://localhost:8000/my_score_all', formData)
        .then(resp => {
          console.log(resp)
          if (resp.data.error === 1) {
            this.$notify({
              title: '失败',
              message: resp.data.msg,
              type: 'error'
            })
          } else {
            var list = resp.data.data
            console.log(this.tableMyScore)
            this.tableMyScore.splice(0, this.tableMyScore.length)
            console.log(this.tableMyScore)
            for (var index in list) {
              console.log(list[index])
              var gpa = ''
              var score = list[index].total_score
              if (score >= 90) {
                gpa = 4.0
              } else if (score >= 85) {
                gpa = 3.7
              } else if (score >= 82) {
                gpa = 3.3
              } else if (score >= 79) {
                gpa = 3.0
              } else if (score >= 60) {
                gpa = 1.0
              } else {
                gpa = 0.0
              }
              this.tableMyScore.push({
                // course_id: '01001234',
                // course_name: '编译原理',
                // teacher_id: '1000',
                // teacher_name: '魏晓',
                // credit: 4,
                // score: 95,
                // gpa: 4.0.toFixed(1)
                course_id: list[index].course_id,
                course_name: list[index].course_name,
                teacher_id: list[index].teacher_id,
                teacher_name: list[index].teacher_name,
                credit: list[index].credit,
                score: list[index].total_score,
                gpa: gpa.toFixed(1)
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

      var credits = 0
      var avgGPA = 0.0
      for (var index in this.tableMyScore) {
        credits += this.tableMyScore[index].credit
        avgGPA += this.tableMyScore[index].gpa * this.tableMyScore[index].credit
        // console.log(avgGPA)
      }
      // console.log(credits)
      // console.log(avgGPA)
      avgGPA = avgGPA / credits
      this.sum_credits = credits
      this.average_gpa = avgGPA.toFixed(1)
      this.isSearch = true
    }
  }
}
</script>

<style scoped>
</style>
