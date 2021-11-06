import Vue from 'vue'
import Router from 'vue-router'
// 这里导入了LoginRegister的export default模块
import login from '../components/login'
import Index from '../components/Index'
import layout from '../views/layout/layout'
import welcome from '../components/Welcome'
import users from '../components/users'
import info from '../components/Info'
import video from '../components/lesson/videoPlayer'
import collapse from '../components/lesson/Collapse'
import catalog from "../components/lesson/catalog";
import study from "../components/lesson/study";
import lessonCard from "../components/lesson/lessonCard";

Vue.use(Router)
// Router实例
const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/lessoncard',
      component: lessonCard
    },
    {
      // 路由与组件绑定
      path: '/login',
      name: 'login',
      component: login,
      meta: {
        title: '用户登录'
      }
    },
// 进入index页面，由于重定向redirect到welcome页面（先展示index组件，由于重定向，会在index页面占位符的位置上显示welcome组件）
    {
      path: '/welcome',
      name: 'index',
      component: Index,
      redirect: '/welcome',
      children: [
        {
          path: '/welcome',
          component: welcome,
          meta: {
            title: '首页'
          }
        },
        {
          path: '/system/users/:id(\\d+)',
          component: info,
          meta: {
            title: '个人中心'
          }
        },
        {
          path: '/system/users/',
          component: users,
          meta: {
            title: '用户管理'
          }
        },
        {
          path: '/lesson/study',
          component: collapse,
          meta: {
            title: '课程学习'
          }
        }
      ]
    },
    {
      path: '/layout',
      name: 'layout',
      component: layout
    },
    {
      path: '/video',
      name: 'videoPlayer',
      component: video
    },
    {
      path: '/collapse',
      name: 'collapse',
      component: collapse
    },
    {
      path: '/catalog',
      component: catalog
    },
    {
      path: '/study',
      component: study
    }
  ]
})

export default router
