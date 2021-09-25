<template>
  <el-container class="home-container">
    <!--  头部区域-->
    <el-header>
      <div>
        <img src=" " alt="">
        <span>执法训练管理平台</span>
      </div>
      <!--      <span>欢迎，username</span>-->
      <el-dropdown trigger="click">
        <span class="header-avatar" style="cursor: pointer">
<!--                      !!!!!!!!这里需要返回用户信息的姓名-->
        <span style="margin-left: 5px ;color: #409EFF;
        font-family:'Microsoft YaHei';font-size: medium">
          {{ this.username }}</span>
          <i class="el-icon-arrow-down"/>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>
            <el-button type="text" @click="getUserInfo">个人中心</el-button>
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
    <!--  页面主体区域-->
    <el-container>
      <!--    侧边栏菜单区域-->
      <!--      随着折叠改变宽度使用判断语句-->
      <el-aside :width="isCollapse?'64px':'200px'">
        <div class="toggle-btn">
          <i class="el-icon-s-unfold" v-show="isCollapse" @click="toggleCollapse"></i>
          <i class="el-icon-s-fold" v-show="!isCollapse" @click="toggleCollapse"></i>
        </div>
        <!--        侧边栏菜单区域-->
        <el-menu background-color="#333744" text-color="#fff"
                 active-text-color="#409EFF"
                 :collapse="isCollapse"
                 :collapse-transition="false"
                 :router="true"
                 unique-opened
                 :default-active="$route.path">
          <!--          未完成！！！！点击菜单列表是需要进行高亮：default-active属性需要根据二级菜单的index改变而改变-->
          <!--          collapse	是否水平折叠收起菜单,默认为false
                        collapse-transition	是否开启折叠动画
                        active-text-color	当前激活菜单的文字颜色（仅支持 hex 格式）
          -->
          <!-- 一级菜单 -->
          <el-submenu :index="'/'+menu.path" v-for="menu in menuList" :key="menu.id">
            <!-- 一级菜单的模板区 -->
            <template slot="title">
              <!-- 图标 -->
              <i :class="menu.icon"></i>
              <!-- 文本 -->
              <span>{{ menu.title }}</span>
            </template>
            <!-- 二级菜单 -->
            <el-menu-item :index="submenu.path" v-for="submenu in menu.children" :key="submenu.id">
              <template slot="title">
                <!-- 图标 -->
                <i :class="submenu.icon"></i>
                <!-- 文本 -->
                <span>{{ submenu.title }}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!--    右侧内容主体-->
      <el-main>
        <!--        路由占位符-->
        <router-view>
        </router-view>
      </el-main>
    </el-container>
  </el-container>

</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      uid: null,
      username: null,
      userInfo: null,
      // 左侧菜单数据
      menuList: [
        {
          "id": 101,
          "authName": "系统管理",
          "path": "users",
          "children": [
            {
              "id": 111,
              "authName": "用户管理",
              "path": "users",
            },
            {
              "id": 121,
              "authName": "权限管理",
              "path": "rights",
            },
            {
              "id": 131,
              "authName": "部门管理",
              "path": "departs",
            },
            {
              "id": 141,
              "authName": "岗位管理",
              "path": "posts",
            },
            {
              "id": 151,
              "authName": "角色管理",
              "path": "roles",
            }
          ]
        },
        {
          "id": 102,
          "authName": "课程管理",
          "path": "lessons",
          "children": [
            {
              "id": 112,
              "authName": "课程列表",
              "path": "lessons",
            },
            {
              "id": 122,
              "authName": "章节列表",
              "path": "chapters",
            },
            {
              "id": 132,
              "authName": "学习课程",
              "path": "learn",
            }
          ]
        },
        {
          "id": 103,
          "authName": "训练管理",
          "path": "trains",
          "children": [
            {
              "id": 113,
              "authName": "训练列表",
              "path": "trains",
            },
            {
              "id": 123,
              "authName": "参加训练",
              "path": "attend",
            }
          ]
        },
        {
          "id": 104,
          "authName": "数据分析",
          "path": "analysis",
          "children": [
            {
              "id": 114,
              "authName": "成绩分析",
              "path": "analysis",
            }
          ]
        },

      ],
      iconsObj: {
        '101': 'el-icon-s-tools',
        '102': 'el-icon-s-order',
        '103': 'el-icon-s-cooperation',
        '104': 'el-icon-s-marketing',
        '111': 'el-icon-user',
        '121': 'el-icon-lock',
        '131': 'el-icon-office-building',
        '141': 'el-icon-house',
        '151': 'el-icon-thumb',
        '112': 'el-icon-notebook-1',
        '122': 'el-icon-notebook-2',
        '132': 'el-icon-data-analysis',
        '113': 'el-icon-mobile',
        '123': 'el-icon-trophy',
        '114': 'el-icon-s-data'
      },
      isCollapse: false
    }
  },
  created() {
    this.uid = sessionStorage.getItem('uid')
    this.username = sessionStorage.getItem('username')
    console.log(sessionStorage.getItem('access'))
    this.getMenuDict()
  },
  methods: {
    // 点击按钮，切换菜单的折叠与展开
    toggleCollapse() {
      this.isCollapse = !this.isCollapse
    },
    // 获取所有菜单
    async getMenuDict() {
      this.$axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/rbac/user/get_menu_button/',
        headers: {
          Authorization: `Bearer ${sessionStorage.getItem('access')}`
        }
      }).then(res => {
        console.log(res.data)
        console.log(res.data['data']['menu_list'])
        this.menuList = this.$utils.toArrayTree(res.data['data']['menu_list'])
        console.log(this.menuList)
      })
    },
    getUserInfo() {
      this.$router.push(`${this.uid}`)
    },
    logout() {
      this.$confirm('确定要退出系统吗？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
          // 退出后清空sessionStorage中的所有内容
          sessionStorage.clear()
          this.$message({
            type: 'success',
            message: '退出成功'
          })
          this.$router.push('/')
        }
      )
    },

  }

}
</script>

<style lang="scss" scoped>
.home-container {
  height: 100%;
}

.el-header {
  background-color: #333744;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  color: #FFFDEF;
  font-size: 20px;
  align-items: center;
}

.el-aside {
  background-color: #333744;
}

.el-menu {
  border-right: none;
}

.el-main {
  background-color: #eaedf1;
}

.toggle-btn {
  background-color: #4a5064;
  color: #ffffff;
  text-align: center;
}
</style>
