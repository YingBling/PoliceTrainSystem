import Vue from 'vue'
import Router from 'vue-router'
// 这里导入了LoginRegister的export default模块
import Login from '../components/Login'
import Index from '../components/Index'
import Navbar from '../components/Navbar'
import HelloWorld from '../components/HelloWorld'

Vue.use(Router)
// Router实例
export default new Router({
  mode: 'history',
  routes: [
    {
      // 路由与组件绑定
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/frametest',
      name: 'frame',
      component: Navbar
    },
    {
      path: '/hello',
      component: HelloWorld
    }
  ]
})
