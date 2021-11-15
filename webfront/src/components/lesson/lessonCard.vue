<template>
  <el-card class="box-card">
    <div class="center1">
      <span class="title">卡通</span>
      <el-button class="button" type="text">开始学习</el-button>
      <div class="details">动画片</div>
    </div>
    <div class="center2">
      <img
        src="http://127.0.0.1:8000/media/CACHE/images/cover/girl_ears_glance_215775_1280x720/5962470167e454184fcd31c4864cacc0.jpg"
        class="image"
      />
    </div>
  </el-card>
</template>

<script>
export default {
  name: "lessonCard"
}
</script>

<style scoped>
.center1 {
  position: absolute;
  width: 80%;
  /*float: right;*/
}

.center2 {
  position: absolute;

  /*width: 40%;*/
  /*float: left;*/
}

.button {
  position: absolute;
  right: 10px;
  float: right;
}

.card-header {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.box-card {
  position: relative;
  float: top;
  width: 400px;
  height: 200px;
}


.image {
  width: 50%;
  display: block;
}

.details {
  position: absolute;
  float: bottom;
  left: auto;
  color: #b1b1b1
}

.title {
  position: absolute;
  float: top;
  max-height: 44px;
  overflow: hidden;
  -o-text-overflow: ellipsis;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 22px;
  color: #333;
  font-size: 16px;
  font-weight: 700;
}

</style>

