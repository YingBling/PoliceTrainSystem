<template>

  <el-container style="border: 1px solid #eee">
    <el-header style="text-align: right; font-size: 14px">
<!--      <h1 style="text-align: center">执法训练管理平台</h1>-->
      <span>欢迎，username</span>
      <el-dropdown>
        <i class="el-icon-setting" style="margin-right: 15px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>
            <el-button type="text" @click="userCenter">个人中心</el-button>
          </el-dropdown-item>
          <el-dropdown-item>
            <el-button type="text" @click="userCenter">个人中心</el-button>
          </el-dropdown-item>
          <el-dropdown-item>
            <el-button type="text" @click="updatePassword">修改密码</el-button>
          </el-dropdown-item>
          <el-dropdown-item>
            <el-button type="text" @click="logout">退出系统</el-button>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </el-header>
    <el-container>
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>系统管理</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">权限管理</el-menu-item>
              <el-menu-item index="1-2">用户管理</el-menu-item>
              <el-menu-item index="1-3">部门管理</el-menu-item>
              <el-menu-item index="1-4">岗位管理</el-menu-item>
              <el-menu-item index="1-5">角色管理</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-link to="/hello">Hello</router-link>
        <!--        用于渲染router-link的内容的容器-->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {}
  },
  methods: {

    logout() {
      this.$confirm('确定要退出系统吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
          localStorage.removeItem('access')
          localStorage.removeItem('refresh')
          this.$message({
            type: 'success',
            message: '退出成功'
          })
          this.$router.push('/')
        }
      )
    }
  }
}
</script>

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
