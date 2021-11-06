<template>
  <!--  <skeleton></skeleton>-->
  <el-collapse v-model="activeNames" @change="handleChange">

    <el-collapse-item v-for="item in chapterList" :title="item['ChapterName']"
                      style="font-family:'Microsoft YaHei',serif;
                        font-size: large;
                        font-weight: bold;">
      <player v-bind:movie_src="item.ChapterFile"></player>
    </el-collapse-item>

  </el-collapse>

</template>

<script>
// 引入组件
import player from "./videoPlayer"
import skeleton from "../skeleton"

export default {
  name: "Collapse",
  components: {
    skeleton,
    player
  },
  data() {
    return {
      chapterList: [
        {
          "id": 1,
          "ChapterID": "test1",
          "ChapterName": "big_buck_bunny",
          "ChapterFile": "http://127.0.0.1:8000/media/lesson/20211009/big_buck_bunny.mp4",
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
