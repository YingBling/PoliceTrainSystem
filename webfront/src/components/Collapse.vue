<template>
  <el-scrollbar
    wrapClass="scrollbar-wrap"
    :style="{height: scrollHeight}"
    ref="scrollbarContainer">


    <el-collapse v-model="activeNames" @change="handleChange">

      <el-collapse-item v-for="item in chapterList" :title="item['ChapterName']"
                        style="font-family:'Microsoft YaHei',serif;
                        font-size: large;
                        font-weight: bold;">
        <player v-bind:movie_src="item.ChapterFile"></player>
      </el-collapse-item>

    </el-collapse>
  </el-scrollbar>
</template>

<script>
import player from '../components/videoPlayer'

export default {
  name: "Collapse",
  components: {
    player
  },
  data() {
    return {
      chapterList: [
        {
          "id": 1,
          "ChapterID": "test1",
          "ChapterName": "big_buck_bunny",
          "ChapterFile": "http://127.0.0.1:8000/media/lesson/20211009/big_buck_bunny_uX3xw0x.mp4",
          "lessons": [],
          "learners": []
        },
        {
          "id": 2,
          "ChapterID": "test2",
          "ChapterName": "乐高大电影2",
          "ChapterFile": "http://127.0.0.1:8000/media/lesson/20211009/190312083533415853.mp4",
          "lessons": [],
          "learners": []
        },
        {
          "id": 3,
          "ChapterID": "test3",
          "ChapterName": "紧急救援",
          "ChapterFile": "http://127.0.0.1:8000/media/lesson/20211009/190319222227698228.mp4",
          "lessons": [],
          "learners": []
        },
        {
          "id": 4,
          "ChapterID": "test4",
          "ChapterName": "trailer",
          "ChapterFile": "http://127.0.0.1:8000/media/lesson/20211009/trailer.mp4",
          "lessons": [],
          "learners": []
        }
      ]
    }
  },

}
</script>

<style scoped>

</style>
