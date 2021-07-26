import Vue from 'vue'
import Router from 'vue-router'
// 这里导入了LoginRegister的export default模块
import LoginRegister from "../components/LoginRegister";
import HelloWorld from "../components/HelloWorld";
import home from "../router/home"
import a from "../router/home"

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      // 路由与组件绑定
      path: '/',
      name: 'login',
      component: LoginRegister
    },
    home,
  ]
})
