<template>
  <div>
    <el-card>
      <div class="course-label">
        <div class="leftImg">
          <img class="imgStyle" :src="lessonBrief.cover_clip" alt="课程名称">
        </div>
        <div class="rightCon">
          <p class="title">{{lessonBrief.LessonName}}</p>
          <p class="teacher">
            <span style="padding-right: 20px">
              <svg-icon icon-class="people" name="mingcheng"/>
              湖北大学
            </span>
            <span style="padding-left: 20px ">
              <svg-icon icon-class="people" name="number"/>
              1000人
            </span>
          </p>
          <p class="info">{{ lessonBrief.detail }}</p>
        </div>
      </div>
    </el-card>
    <el-card style="margin:20px 0">
      <div class="course-preview">
        <span style="font-size: 14px;color: #999">学习进度</span>
        <div class="learning-process">
          <el-progress :text-inside="true" :stroke-width="15" :percentage="progress" status="success">
          </el-progress>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  computed: {
    progress() {
      // 计算该学员当前完成的进度
      return (this.finished / this.total * 100)
    }
  },
  data() {
    return {
      total: 10,
      finished: 8
    }
  },
  props: {
    lessonBrief: Object
  }
}
</script>

<style lang="scss" scoped>
.course-label {
  min-height: 200px;
  padding: 20px;
  border-radius: 4px;
  margin: -10px;
  display: flex;
}

.leftImg {
  width: 300px;
  height: 180px;
  border-radius: 4px;
  margin: 20px;
}

.imgStyle {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 4px;
  position: relative;
}

.rightCon {
  padding: 20px;
  margin: 10px;
}

.title {
  margin-top: 8px;
  font-size: 16px;
  font-weight: 500;
  color: #333;
}

.teacher {
  padding: 12px 0;
  color: #999;
  font-size: 12px;
}

.info {
  font-size: 14px;
  color: #999;
  line-height: 22px;
  height: 66px;
  overflow: hidden;
  position: relative;
}

.course-preview {
  display: flex;
  height: 20px;
  line-height: 20px;
}

.learning-process {
  padding-left: 15px;
  width: 90%;
}
</style>
