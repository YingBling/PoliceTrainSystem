<template>
  <div class="app-container">
    <Brief :lessonBrief="lessonBrief"></Brief>
    <div class="course-tab">
      <el-card>
        <el-tabs v-model="activeName" @tab-click="handleTab">
          <el-tab-pane
            v-for="(tab, index) in tabs"
            :key="index"
            :label="tab.label"
            :name="tab.name"
          >
            <component
              :is="tab.name"
              v-if="tab.name === nowTab"
              :param="param"
            ></component>
          </el-tab-pane>
        </el-tabs>
      </el-card>
    </div>
  </div>
</template>

<script>
import Brief from '@/views/lesson/study/detail/components/Brief'
import Intro from '@/views/lesson/study/detail/components/Intro'
import ChapterList from '@/views/lesson/study/detail/components/ChapterList'
import Player from '@/views/lesson/study/detail/components/VideoPlayer'
import Catalogue from '@/views/lesson/study/detail/components/Catalogue'

export default {
  name: 'StudyDetail',
  components: { Player, ChapterList, Intro, Brief, Catalogue },
  data() {
    return {
      activeName: 'Intro',
      param: '', // 要传递的参数
      isPlay: false,
      lessonBrief: {},
      chapterList: [],
      nowTab: 'Intro',
      tabs: [
        {
          name: 'Intro',
          label: '课程介绍'
        },
        {
          name: 'Catalogue',
          label: '课程目录'
        }
      ]
    }
  },
  mounted() {
    this.$axios
      .get('http://127.0.0.1:8000/api/lesson/lesson/get_brief', {
        params: {
          id: this.$route.query.id
        }
      })
      .then((response) => {
        console.log(response.data)
        this.lessonBrief = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    this.$axios
      .get('http://127.0.0.1:8000/api/lesson/lesson/get_chapterByLesson/', {
        headers: {},
        params: {
          id: this.$route.query.id
        }
      })
      .then((response) => {
        const { data } = response
        this.chapterList = data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    handleTab(tab) {
      // 根据tab传递参数
      this.nowTab = tab.name
      console.log(tab.name)
      if (tab.name === 'Catalogue') {
        this.param = this.chapterList
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.el-scrollbar__wrap {
  overflow-x: hidden;
}
</style>
