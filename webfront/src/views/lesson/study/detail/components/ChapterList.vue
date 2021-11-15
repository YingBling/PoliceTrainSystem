<template>
  <div class="chapterList">
    <el-menu
      :default-active="chapterList.index"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">
      <el-submenu :index="chap.id+''" v-for="(chap,index) in chapterList" :key="chap.id">
        <template slot="title">
          <span>第{{ index + 1 }}章</span>
        </template>
        <el-menu-item :index="chap.ChapterFile" @click="handleClick(chap.ChapterFile)">
           <span class="svg-container" style="padding-right: 8px">
            <svg-icon icon-class="finish"  v-if="index%2===0"/>
            <svg-icon icon-class="unfinish" v-else/>
          </span>
          {{ chap.ChapterName }}
        </el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'ChapterList',
  data() {
    return {
      isfinish: true
    }
  },
  props: {
    chapterList: Array
  },
  mounted() {
  },
  methods: {
    handleOpen() {
      console.log('open')
    },
    handleClose() {
      console.log('close')
    },
    handleClick(url) {
      this.$bus.$emit('playMovie', { url: url })
    }

  }
}
</script>

<style lang="scss" scoped>
.el-menu-item{
  overflow: hidden;
  text-overflow:ellipsis ;
}
</style>
