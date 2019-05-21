<template>
  <div id="app">
    <div>
      <el-menu
        router
        v-show="isAdmin"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item style="color: red; font-size: 20px; bold: true">管理员</el-menu-item>
        <el-menu-item index="AdminStudent">维护学生信息</el-menu-item>
        <el-menu-item index="AdminTeacher">维护教师信息</el-menu-item>
        <el-menu-item index="AdminCourse">维护课程信息</el-menu-item>
        <el-menu-item index="AdminSearchCourse">查询课程情况</el-menu-item>
        <el-menu-item index="AdminSettings">设置</el-menu-item>
      </el-menu>
      <el-menu
        router
        v-show="isStudent"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item style="color: yellow; font-size: 20px; bold: true">学生</el-menu-item>
        <el-menu-item index="StudentSearchCourse">课程查询</el-menu-item>
        <el-menu-item index="StudentChooseCourse">选课</el-menu-item>
        <el-menu-item index="StudentQuitCourse">退课</el-menu-item>
        <el-menu-item index="StudentMyCourse">我的课表</el-menu-item>
        <el-menu-item index="StudentMyScore">我的成绩</el-menu-item>
      </el-menu>
      <el-menu
        router
        v-show="isTeacher"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item style="color: yellow; font-size: 20px; bold: true">教师</el-menu-item>
        <el-menu-item index="TeacherSearchCourse">课程查询（自己开的课）</el-menu-item>
        <el-menu-item index="TeacherUploadScore">上传成绩</el-menu-item>
        <el-menu-item index="TeacherSearchGrade">成绩汇总</el-menu-item>
      </el-menu>
    </div>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {},
  data: function () {
    return {
      isStudent: false,
      isTeacher: false,
      isAdmin: false
    }
  },
  created: function () {
    this.isStudent = JSON.parse(localStorage.getItem('isStudent'))
    this.isTeacher = JSON.parse(localStorage.getItem('isTeacher'))
    this.isAdmin = JSON.parse(localStorage.getItem('isAdmin'))
  },
  methods: {}
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
