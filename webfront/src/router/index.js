import Vue from 'vue'
import Router from 'vue-router'
// 这里导入了LoginRegister的export default模块
import login from '../components/login'
import Index from '../components/Index'
import layout from '../views/layout/layout'
import welcome from '../components/Welcome'
import users from '../components/users'

Vue.use(Router)
// Router实例
const router = new Router({
  mode: 'history',
  routes: [
    {path:'/',redirect:'/login'},
    {
      // 路由与组件绑定
      path: '/login',
      name: 'login',
      component: login
    },
// 进入index页面，由于重定向redirect到welcome页面（先展示index组件，由于重定向，会在index页面占位符的位置上显示welcome组件）
    {
      path: '/index',
      name: 'index',
      component: Index,
      redirect:'/welcome',
      children:[
        { path:'/welcome',
          component:welcome
        },
        {
          path:'/users',
          component:users
        }
        ]
    },
    {
      path: '/layout',
      name: 'layout' ,
      component: layout
    },
  ]
})

export default router
