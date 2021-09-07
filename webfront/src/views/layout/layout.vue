<template>
<el-container class="layout-cont">
  <el-container :class="[isSider?'openside':'hideside',isMobile ? 'mobile':'']">
<!--    侧边菜单栏-->
  <el-aside class="main-cont main-left">
<!--    侧边菜单标题栏-->
    <div class="title">
      <img class="logoimg" src="../../assets/images/logo.png" alt="">
      <h2 v-if="isSider" class="tit-text" >管理系统</h2>
    </div>
<!--    菜单-->
    <Aside class="aside"/>
  </el-aside>
<!--    分块滑动功能-->
    <el-main class="main-cont main-right">
      <transition :duration="{enter: 800, leave: 100}" mode="out-in" name="el-fade-in-liner">
<!--      内置组件transition>name：el-fade-in-linear 和 el-fade-in 两种过渡动画效果：淡入淡出-->
<!--      mode：控制离开/进入过渡的时间序列。有效的模式有 "out-in" 和 "in-out"-->
<!--      duration ： 指定过渡的持续时间-->
        <div
          :style="{width: `calc(100% - ${isMobile?'0px':isCollapse?'54px':'220px'})`}"
          class="topfix">
<!--          导航栏头部-->
          <el-row>
            <el-header class="header-cont">
<!--              hamburger:菜单栏的收缩与展开-->
              <el-col :xs="2" :lg="1" :md="1" :sm="1" :xl="1">
                <div class="menu-total" @click="totalCollapse">
                    <i v-if="isCollapse" class="el-icon-s-unfold" />
                    <i v-else class="el-icon-s-fold" />
                </div>
              </el-col>
<!--              breadcrumb:面包屑-->
              <el-col :xs="10" :lg="14" :md="14" :sm="9" :xl="14">
                <el-breadcrumb class="breadcrumb" separator-class="el-icon-arrow-right">
                  <el-breadcrumb-item>
<!--                  v-for="item in matched.slice(1,matched.length) "-->
<!--                  :key="item.path">-->
<!--                    {{item.meta.title}}-->
                    <p>这里是面包屑</p>
                  </el-breadcrumb-item>
<!--                  $route.matched:包含当前路由的所有嵌套路径片段的路由记录-->
<!--                  JavaScript操作数组的方法slice(切片起始位置 ,结束位置（不包括）)-->
                </el-breadcrumb>
              </el-col>
              <el-col :xs="12" :lg="9" :md="9" :sm="14" :xl="9">
                <div class="fl-right right-box">
                  <el-dropdown trigger="click">
<!--                    用户名称，也可以加用户头像-->
                    <span class="header-avatar" style="cursor: pointer">
<!--                      !!!!!!!!这里需要返回用户信息的姓名-->
                        <span style="margin-left: 5px">summer</span>
                        <i class="el-icon-arrow-down" />
                    </span>
<!--                    下拉菜单-个人中心/退出登录-->
                    <el-dropdown-menu slot="dropdown" class="dropdown-group">
                      <el-dropdown-item icon="el-icon-s-custom" @click.native="toPerson">个人中心</el-dropdown-item>
                      <el-dropdown-item icon="el-icon-switch-button" @click.native="LoginOut">退出登录</el-dropdown-item>
                    </el-dropdown-menu>
                  </el-dropdown>
                </div>
              </el-col>

            </el-header>
          </el-row>
        </div>
      </transition>
    </el-main>
  </el-container>

</el-container>
</template>

<script>
import Aside from '@/views/layout/aside'
export default {
  name: "layout",
  components:{
    Aside
  },
  data(){
    return {
      isCollapse:false,
      isSider:false,
      isMobile:false
    }
  },
   mounted() {
    const screenWidth = document.body.clientWidth
    if (screenWidth < 1000) {
      this.isMobile = true
      this.isSider = false
      this.isCollapse = true
    } else if (screenWidth >= 1000 && screenWidth < 1200) {
      this.isMobile = false
      this.isSider = false
      this.isCollapse = true
    } else {
      this.isMobile = false
      this.isSider = true
      this.isCollapse = false
    }
    window.onresize = () => {
      return (() => {
        const screenWidth = document.body.clientWidth
        if (screenWidth < 1000) {
          this.isMobile = true
          this.isSider = false
          this.isCollapse = true
        } else if (screenWidth >= 1000 && screenWidth < 1200) {
          this.isMobile = false
          this.isSider = false
          this.isCollapse = true
        } else {
          this.isMobile = false
          this.isSider = true
          this.isCollapse = false
        }
      })()
    }
  },
  methods:{
    totalCollapse() {
      this.isCollapse = !this.isCollapse
      this.isSider = !this.isCollapse
      this.isShadowBg = !this.isCollapse
      this.$bus.emit('collapse', this.isCollapse)
    },
    toPerson() {
      this.$router.push('/users')
    },

  }
}
</script>

<style lang="scss" scoped>
@import "../../style/mobile";
</style>
