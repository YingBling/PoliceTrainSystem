// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import axios from 'axios'
import Router from "vue-router";

Vue.use(ElementUI)
Vue.use(VueResource)
Vue.use(Router)

// axios.defaults.baseURL = 'http://127.0.0.1:8000/api/user/'
Vue.prototype.$axios = axios // 全局注册，使用方法为:this.$axios
/* eslint-disable no-new */

router.beforeEach((to, from, next) => {
  window.document.title = to.meta.title == undefined ? '执法训练管理平台' : to.meta.title

    next();
})
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})

