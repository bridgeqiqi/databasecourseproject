import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AdminStudent from '@/components/Admin_Student'
import AdminCourse from '@/components/Admin_Course'
import AdminSearchCourse from '@/components/Admin_SearchCourse'
import AdminSettings from '@/components/Admin_Settings'
import AdminTeacher from '@/components/Admin_Teacher'
import StudentChooseCourse from '@/components/Student_ChooseCourse'
import StudentMyCourse from '@/components/Student_MyCourse'
import StudentMyScore from '@/components/Student_MyScore'
import StudentQuitCourse from '@/components/Student_QuitCourse'
import StudentSearchCourse from '@/components/Student_SearchCourse'
import TeacherSearchCourse from '@/components/Teacher_SearchCourse'
import TeacherSearchGrade from '@/components/Teacher_SearchGrade'
import TeacherUploadScore from '@/components/Teacher_UploadScore'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/App',
      name: 'App',
      component: () => import('../App.vue'),
      children: [
        {
          path: '/AdminStudent',
          name: 'AdminStudent',
          component: AdminStudent
        },
        {
          path: '/AdminTeacher',
          name: 'AdminTeacher',
          component: AdminTeacher
        },
        {
          path: '/AdminCourse',
          name: 'AdminCourse',
          component: AdminCourse
        },
        {
          path: '/AdminSearchCourse',
          name: 'AdminSearchCourse',
          component: AdminSearchCourse
        },
        {
          path: '/AdminSettings',
          name: 'AdminSettings',
          component: AdminSettings
        },
        {
          path: '/StudentSearchCourse',
          name: 'StudentSearchCourse',
          component: StudentSearchCourse
        },
        {
          path: '/StudentChooseCourse',
          name: 'StudentChooseCourse',
          component: StudentChooseCourse
        },
        {
          path: '/StudentQuitCourse',
          name: 'StudentQuitCourse',
          component: StudentQuitCourse
        },
        {
          path: '/StudentMyCourse',
          name: 'StudentMyCourse',
          component: StudentMyCourse
        },
        {
          path: '/StudentMyScore',
          name: 'StudentMyScore',
          component: StudentMyScore
        },
        {
          path: '/TeacherSearchCourse',
          name: 'TeacherSearchCourse',
          component: TeacherSearchCourse
        },
        {
          path: '/TeacherUploadScore',
          name: 'TeacherUploadScore',
          component: TeacherUploadScore
        },
        {
          path: '/TeacherSearchGrade',
          name: 'TeacherSearchGrade',
          component: TeacherSearchGrade
        }
      ]
    }
  ]
})
