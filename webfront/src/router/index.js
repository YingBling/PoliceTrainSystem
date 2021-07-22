import Vue from 'vue'
import Router from 'vue-router'
import LoginRegister from '../components/LoginRegister'

Vue.use(Router)

export default new Router({
  routes: [
    // 通过redirect重定向，当用户访问localhost：8080不需要输入login直接定位进入登录页面
    {path:'/',redirect:'/login'},
    {
      path: '/login',
      name: 'LoginRegister',
      component: LoginRegister
    }
  ]
})
