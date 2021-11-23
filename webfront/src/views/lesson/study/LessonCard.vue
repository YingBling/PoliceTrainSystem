<template>
  <div>
    <el-card shadow="hover" :body-style="{ padding: '0px' } ">
      <img class="item-image" :src="lesson.cover_clip">
      <div class="item-body">
        <div class="item-title">
          <router-link
            :to="{
              path:'/lesson/study/detail/studyDetail',
              headers:{
                authorization:''
              },
              query:{
                id:lesson.id
              }
            }">
            {{ lesson.LessonName }}
          </router-link>
        </div>
        <div class="item-desc">{{ lesson.detail }}</div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'LessonCard',

  data() {
    return {}
  },
  mounted() {
  },
  methods: {},
  props: {
    lesson: Object
  }
}
</script>

<style lang="scss" scoped>

.item-image {
  width: 100%;
  display: block;
}

.item-body {
  padding: 20px 12px 10px;
}

.item-title {
  font-size: 16px;
  margin-bottom: 12px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #333333;
  font-weight: 500;
}

.item-title:hover {
  cursor: pointer;
  color: #409EFF;
}

.item-desc {
  color: #666;
  font-size: 12px;
  margin-bottom: 4px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

</style>

