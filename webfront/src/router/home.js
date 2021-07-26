import Vue from 'vue'
import Router from 'vue-router'
// 这里导入了LoginRegister的export default模块
import LoginRegister from "../components/LoginRegister";
import Home from "../components/Home"


Vue.use(Router)

const home = {
  path: '/home',
  name: 'home',
  component: Home
};
export default home


