<template>
  <div class="app-container">
    <el-table :data="courseList" border>
      <el-table-column
        prop="id"
        label="序号"
        width="70"
        align="center">
      </el-table-column>
      <el-table-column prop="title" label="课程名称" />
      <el-table-column prop="status" label="课程状态" width="100">
        <template  slot-scope="scope">
          <el-tag type="success" v-if="scope.row.status === 1">已发布</el-tag>
          <el-tag type="danger" v-else>未发布</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="lessonNum" label="课时数" width="100"/>
      <el-table-column prop="gmtCreate" label="添加时间" width="160"/>
      <el-table-column label="操作" width="200" align="center">
        <template slot-scope="scope">
          <el-button type="danger" size="mini" icon="el-icon-delete"  @click="removeDataById(scope.row.id)">删除课程</el-button>
        </template>
      </el-table-column>
    </el-table>
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
</template>

<script>
export default {
  name: 'LessonSyS',
  data() {
    return {
      total: 0,
      currentPage: 1,
      limit: 10,
      courseList: [{
        'id': 1,
        'title': 'java从入门到精通',
        'status': 1,
        'lessonNum': '20',
        'gmtCreate': '2021/11/10 11:00'
      }, {
        'id': 2,
        'title': 'java从入门到精通',
        'status': 1,
        'lessonNum': '20',
        'gmtCreate': '2021/11/10 11:00'
      }, {
        'id': 3,
        'title': 'Vue2.0',
        'status': 0,
        'lessonNum': '40',
        'gmtCreate': '2021/11/10 11:00'
      }, {
        'id': 4,
        'title': 'Python从入门到精通',
        'status': 1,
        'lessonNum': '20',
        'gmtCreate': '2021/11/10 11:00'
      }, {
        'id': 5,
        'title': 'c++教程',
        'status': 0,
        'lessonNum': '20',
        'gmtCreate': '2021/11/10 11:00'
      }]
    }
  },
  methods: {
    getCourseList() {
      this.currentPage = 1
      this.limit = 5
    },
    removeDataById(id) {
      this.$confirm('此操作将永久删除该课程, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(
        this.$message({
          type: 'success',
          message: '删除成功'
        }))
    }
  }
}
</script>

<style scoped>

</style>
