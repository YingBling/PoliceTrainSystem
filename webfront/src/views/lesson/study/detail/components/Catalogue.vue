<template>
  <div class="catalogue" style="display: flex;height: 600px">
    <div class="chap" v-infinite-scroll="load" style="overflow-x:hidden;width: 20%">
      <ChapterList :chapterList="param"></ChapterList>
    </div>
    <div class="player" style="width:65%;margin: 50px">
      <Player v-if="isPlay" :movie_src="movie_src"></Player>
      <el-empty v-else description="请选择要学习的章节"></el-empty>
    </div>

  </div>
</template>

<script>
import ChapterList from '@/views/lesson/study/detail/components/ChapterList'
import Player from '@/views/lesson/study/detail/components/VideoPlayer'

export default {
  name: 'Catelogue',
  components: { Player, ChapterList },
  mounted() {
    // 监听playMovie事件
    this.$bus.$on('playMovie', ({ url }) => {
      this.isPlay = true
      this.movie_src = url
    })
  },
  data() {
    return {
      isPlay: false,
      movie_src: ''
    }
  },
  props: {
    // param是从Study页面接受到的参数，需要传给ChapterList组件
    param: Array
  }
}
</script>

<style lang="scss" scoped>
</style>
