<!--ui结构-->
<template>
  <div id="app" style="overflow: auto">
    <router-view/>
  </div>
</template>
<!--行为-->
<script>
export default {
  name: 'App'
}
</script>
<!--样式-->
<style lang="scss"  scoped="scoped">
//引入初始化样式
@import "/style/main.scss";
@import "style/base.scss";
@import "style/mobile.scss";
#app {
  background: #eee;
  height: 100vh;
  overflow: hidden;
  font-weight: 400 !important;
}
.el-button{
  font-weight: 400 !important;
}
</style>
