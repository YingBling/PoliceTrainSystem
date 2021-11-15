<template>
  <div class="dashboard-container">
<!--    <div class="dashboard-text">name: {{ name }}</div>-->
<!--    <div class="dashboard-text">roles: <span v-for="role in roles" :key="role">{{ role }}</span></div>-->
    <el-avatar src="https://q1.qlogo.cn/g?b=qq&amp;nk=190848757&amp;s=640" class="user-avatar"></el-avatar>
    <div class="title">
      <h1>{{ name }},欢迎您,开始您一天的工作吧！</h1>
      <span> 今日晴，20℃ - 32℃！ </span>
    </div>
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>模块一：todo清单</span>
          </div>
          <el-row>
            <el-col :span="8"></el-col>
          </el-row>
        </el-card>
<!--        卡片2区域-->
        <el-card class="box-card" style="margin-top: 25px">
          <div slot="header" class="clearfix">
            <span>模块2：训练动态</span>
            <el-button style="float: right; padding: 3px 0" type="text">更多</el-button>
          </div>
          <el-row>
            <el-col :span="24">
              <el-avatar :src="avatar" size="small" :key="index" class="activity-avatar"></el-avatar>
              <el-divider></el-divider>
            </el-col>
          </el-row>
        </el-card>
      </el-col>

      <el-col :span="12">
        <div class="grid-content bg-purple">

          <el-card class="box-card" >
            <div slot="header" class="clearfix">
              <span>课程学习情况</span>
            </div>
            <el-row>
              <el-col :span="8">
                <el-card shadow="hover">
                </el-card>
              </el-col>
            </el-row>
          </el-card>
          <el-card class="box-card"  style="margin-top: 25px">
            <div slot="header" class="clearfix">
              <span>数据统计分析</span>
            </div>

            <div>
              <v-chart class="chart" :option="option" />
            </div>
          </el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  }
}
</script>

<style lang="scss" scoped>
    .user-avatar{
        //width: $userAvatarLength;
        //height: $userAvatarLength;
        //line-height: $userAvatarLength;
      display: inline-block;
    }
    .title{
      display: inline-block;
      padding: 0 0 0 15px;
      position: relative;
      top: -5px;

      h1{
        font-size: 1.125rem;
        font-weight: 500;
        line-height: 1.75rem;
      }
      span{
        font-size: 14px;
        color: rgba(0,0,0,.45);
      }
    }
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
