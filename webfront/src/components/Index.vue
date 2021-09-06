<template xmlns:disabled="http://www.w3.org/1999/xhtml">
  <div id="index">
    <Navbar></Navbar>
  </div>
</template>

<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>

<script>
import Navbar from '../components/Navbar'

export default {
  components: {Navbar},
  data() {
    const item = {
      date: '2016-05-02',
      name: '王小虎',
      address: '上海市普陀区金沙江路 1518 弄'
    }
    return {
      tableData: Array(20).fill(item)
    }
  }
}
</script>
<!--<script>-->
<!--export default {-->
<!--  name: 'index',-->
<!--  created() {-->
<!--    // 刷新页面后调用created方法-->
<!--    // 请求所有的用户数据-->
<!--    this.$axios({-->
<!--      method: 'get',-->
<!--      url: 'http://127.0.0.1:8000/rbac/user/list/',-->
<!--      headers: {-->
<!--        // 设置请求头中的Authorization字段，每次发起请求时携带token-->
<!--        'Authorization': 'Bearer ' + localStorage.getItem('access')-->
<!--      }-->
<!--    })-->
<!--      .then(resp => {-->
<!--        if (resp.data['code'] === 200) {-->
<!--          // this.msg = resp.data-->
<!--          this.tableData = resp.data['data']-->
<!--          this.loading = false-->
<!--          // this.status = true-->
<!--        } else {-->
<!--          this.msg = '获取用户信息出错'-->
<!--        }-->
<!--      })-->
<!--      .catch(err => {-->
<!--        alert('由于长时间未响应，请重新登录系统')-->
<!--        this.$router.push('/')-->
<!--        console.log(err)-->
<!--      })-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      tableData: [],-->
<!--      loading: true,-->
<!--      status: false-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--.el-header, .el-footer {-->
<!--  background-color: #B3C0D1;-->
<!--  color: #333;-->
<!--  text-align: center;-->
<!--  line-height: 60px;-->
<!--}-->

<!--.el-aside {-->
<!--  background-color: #D3DCE6;-->
<!--  color: #333;-->
<!--  text-align: center;-->
<!--  line-height: 200px;-->
<!--}-->

<!--.el-main {-->
<!--  background-color: #E9EEF3;-->
<!--  color: #333;-->
<!--  text-align: center;-->
<!--  line-height: 160px;-->
<!--}-->

<!--body > .el-container {-->
<!--  margin-bottom: 40px;-->
<!--}-->

<!--.el-container:nth-child(5) .el-aside,-->
<!--.el-container:nth-child(6) .el-aside {-->
<!--  line-height: 260px;-->
<!--}-->

<!--.el-container:nth-child(7) .el-aside {-->
<!--  line-height: 320px;-->
<!--}-->
<!--</style>-->
