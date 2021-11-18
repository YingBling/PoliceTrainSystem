<template>
  <div class="course-list" style="padding-top: 25px;margin-left:40px;margin-right: -50px">
    <el-row>
      <el-col
        :span="6"
        v-for="lessonObj in LessonList"
              :key="lessonObj.id"
              :offset="1"
              style="margin-bottom: 25px">
        <LessonCard :lesson="lessonObj" :key="lessonObj.id"></LessonCard>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import LessonCard from '@/views/lesson/study/LessonCard'

export default {
  name: 'LessonList',
  components: { LessonCard },
  props: {
    LessonList: Array
  }
}
</script>

<style lang="scss" scoped>
</style>
