<template>
  <div class="app-container">
    <div class="pageContainer">
      <!--      分类栏-->
      <el-card class="box-card">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="我的课程" name="myClass">
            <div class="my-course-box">
              <div class="marBom" style="padding-top: 10px">
                <div class="titleWrap">
                  <span class="classifyTitle">课程类型</span>
                </div>
                <div class="curStyle">
                  <span>全部</span>
                  <span>基础课程</span>
                  <span>案例课程</span>
                </div>
              </div>
              <div class="marBom">
                <div class="titleWrap">
                  <span class="classifyTitle">课程状态</span>
                </div>
                <div class="curStyle">
                  <span>全部</span>
                  <span>进行中</span>
                  <span>已结束</span>
                  <span>未开始</span>
                </div>
              </div>
              <el-divider></el-divider>
            </div>
          </el-tab-pane>
          <el-tab-pane label="课程大厅" name="classList">
            <div class="course-box">
              <div class="marBom" style="padding-top: 10px">
                <div class="titleWrap">
                  <span class="classifyTitle">课程类型</span>
                </div>
                <div class="curStyle">
                  <span>全部</span>
                  <span>基础课程</span>
                  <span>案例课程</span>
                </div>
              </div>
              <el-divider></el-divider>
            </div>
          </el-tab-pane>
        </el-tabs>
      </el-card>
      <!--      搜索框-->
      <div class="search-wrapper" style="margin-top: 30px;padding-left: 20px">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input placeholder="快速查找" :model="input" autocomplete="off"/>
          </el-col>
          <el-col :span="1.5">
            <el-button type="primary" icon="el-icon-search">查询</el-button>
          </el-col>
          <el-col :span="1.5">
            <el-button type="primary" icon="el-icon-refresh">重置</el-button>
          </el-col>
        </el-row>
      </div>
      <el-empty description="暂无数据" v-if="no_data"></el-empty>
      <!--            课程列表-->
      <LessonList :LessonList="LessonList" v-else></LessonList>

      <div class="pagination-container">
        <el-pagination
            :current-page="currentPage"
            :page-size="limit"
            layout='total, prev, pager, next, jumper'
            :total="total"
            style="text-align: right;margin-top: 30px"
            @current-change="getCourseList"/>
      </div>
    </div>
  </div>

</template>

<script>
import LessonList from '@/views/lesson/study/LessonList'

export default {
  name: 'Study',
  components: { LessonList },
  // eslint-disable-next-line vue/no-unused-components

  data() {
    return {
      total: 0,
      currentPage: 1,
      limit: 10,
      input: '',
      activeName: 'myClass',
      ruleForm: '',
      no_data: true,
      token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MTIxMzE4LCJqdGkiOiIyNGFmNWZlNDhmOWE0MTk1YTlmZWYzZDE5MGE2NmUwOSIsInVzZXJuYW1lIjoieWFuZ3l1In0.fLZIXh5KdJtfx7lnwmqEezH-0pBrWDqjcscGoUYLW14',
      LessonList: []
    }
  },
  mounted() {
    // 向后端发网络请求，获取所有的课程
    this.getAllLessons()
  },
  methods: {
    getAllLessons() {
      this.$axios.get('http://127.0.0.1:8000/api/lesson/lesson/',
        {
          headers: {
            authorization: `Bearer ${this.token}`
          }
        }).then((response) => {
        const { data } = response
        this.LessonList = data.results
        this.no_data = false
      }).catch((error) => {
        console.log(error)
      })
    },
    handleClick(tab, event) {
      console.log(tab, event)
    },
    getCourseList() {
      this.currentPage = 1
      this.limit = 5
    }
  }
}
</script>

<style lang="scss" scoped>
.marBom {
  margin-bottom: 25px;
  display: flex;
  font-size: 14px;
  padding: 0 20px;
}

.titleWrap {
  width: 75px;
  text-align: center;
}

.classifyTitle {
  color: #333333;
}

.curStyle {
  width: calc(100% - 75px);
}

.curStyle span {
  margin-right: 8px;
  padding-left: 7px;
  padding-right: 7px;
}

.el-card {
  padding: 0;
  margin-bottom: 20px;
}
.item-footer {
  padding: 10px 12px 20px;
  height: 20px;
  margin-bottom: 10px;
  line-height: 20px;
  color: rgba(0, 0, 0, .45);
  font-size: 12px;
  display: flex;
}

.imgType {
  width: 70%;
}

.imgCount {
  width: 30%;
}

.svg-icon {
  margin-right: 4px;
}
</style>
