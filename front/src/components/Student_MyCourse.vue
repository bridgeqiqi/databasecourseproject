<template>
  <div>
    <div>Student_MyCourse</div>
    <el-table
      :data="tableMyCourse"
      stripe
      fit
      style="margin: 0 auto; width: 90%; text-align:center;">
      <el-table-column prop="index" label="序号" width="150">
      </el-table-column>
      <el-table-column prop="class_time" label="上课时间" width="150">
      </el-table-column>
      <el-table-column prop="monday" label="星期一" width="150">
      </el-table-column>
      <el-table-column prop="tuesday" label="星期二" width="150">
      </el-table-column>
      <el-table-column prop="wednesday" label="星期三" width="150">
      </el-table-column>
      <el-table-column prop="thursday" label="星期四" width="150">
      </el-table-column>
      <el-table-column prop="friday" label="星期五" width="150">
      </el-table-column>
      <el-table-column prop="saturday" label="星期六" width="150">
      </el-table-column>
      <el-table-column prop="sunday" label="星期日" width="150">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tableMyCourse: [{
        index: 1,
        class_time: '8:00-8:45',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 2,
        class_time: '8:45-9:40',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 3,
        class_time: '10:00-10:45',
        monday: '数据库原理',
        tuesday: '',
        wednesday: '离散数学',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 4,
        class_time: '10:55-11:40',
        monday: '数据库原理',
        tuesday: '',
        wednesday: '离散数学',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 5,
        class_time: '12:10-12:55',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 6,
        class_time: '13:05-13:50',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 7,
        class_time: '14:10-14:55',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 8,
        class_time: '15:05-15:50',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 9,
        class_time: '16:00-16:45',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 10,
        class_time: '16:55-17:40',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 11,
        class_time: '18:00-18:45',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 12,
        class_time: '18:55-19:40',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }, {
        index: 13,
        class_time: '19:50-20:35',
        monday: '',
        tuesday: '',
        wednesday: '',
        thursday: '',
        friday: '',
        saturday: '',
        sunday: ''
      }]
    }
  },
  created: function () {
  }
}
</script>

<style scoped>
</style>
