import Vue from 'vue'

import 'normalize.css/normalize.css' // A modern alternative to CSS resets

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en' // lang i18n

import '@/styles/index.scss' // global css
import VideoPlayer from 'vue-video-player' // 导入视频播放插件
import TreeTable from 'vue-table-with-tree-grid'
import vuescroll from 'vuescroll' // 导入滚动条插件
import 'vuescroll/dist/vuescroll.css'
require('vue-video-player/src/custom-theme.css')
require('video.js/dist/video-js.css')
import App from './App'
import store from './store'
import router from './router'
import axios from 'axios'
import { getToken } from "@/utils/auth"
import vuex from 'vuex'

import '@/icons' // icon
import '@/permission' // permission control
/**
 * If you don't want to use mock-server
 * you want to use MockJs for mock api
 * you can execute: mockXHR()
 *
 * Currently MockJs will be used in the production environment,
 * please remove it before going online ! ! !
 */
// 注释掉mock生成数据
// if (process.env.NODE_ENV === 'production') {
//   const { mockXHR } = require('../mock')
//   mockXHR()
// }

// set ElementUI lang to EN
Vue.use(ElementUI, { locale })
Vue.use(VideoPlayer)
Vue.use(vuescroll)
Vue.use(vuex)
Vue.component('tree-table', TreeTable)
// 如果想要中文版 element-ui，按如下方式声明
// Vue.use(ElementUI)
Vue.prototype.$axios = axios
Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
  beforeCreate() {
    // 全局事件总线
    // A与B是兄弟，B要给A发送信息,A收到信息以后打印出来
    // A.$bus.$on('sendMessage',console.log(message))
    // B.$bus.$emit('sendMessage',message)
    Vue.prototype.$bus = this
  }
}).$mount('#app')
