<template>
  <div>
    <el-scrollbar style="height:calc(100vh - 64px)">
      <transition :duration="{ enter: 800, leave: 100 }" mode="out-in" name="el-fade-in-linear">
         <el-menu background-color="#333744" text-color="#fff"
                 active-text-color="#409EFF"
                 :collapse="isCollapse"
                 :collapse-transition="false"
                 router
                 unique-opened
                 default-active="/users">
<!--          未完成！！！！点击菜单列表是需要进行高亮：default-active属性需要根据二级菜单的index改变而改变-->
          <!--          collapse	是否水平折叠收起菜单,默认为false
                        collapse-transition	是否开启折叠动画
                        active-text-color	当前激活菜单的文字颜色（仅支持 hex 格式）
          -->
          <!-- 一级菜单 -->
          <el-submenu  :index="key" v-for="(value,key,i) in menuDict" :key="i" >
            <!-- 一级菜单的模板区 -->
            <template slot="title">
              <!-- 图标 -->
              <i :class="iconsObj[key]"></i>
              <!-- 文本 -->
              <span>{{value['title']}}</span>
            </template>
            <!-- 二级菜单 -->
            <el-menu-item  index="/users" v-for="item in value['children']">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-menu"></i>
                <!-- 文本 -->
                <span>{{ item.title }}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </transition>
    </el-scrollbar>
  </div>
</template>

<script>

export default {
  name: 'Aside',
  data() {
    return {
      // 左侧菜单数据
      menuDict:{},
      iconsObj:{
        '1':'el-icon-reading',
        '2':'el-icon-setting',
        '3':'el-icon-attract',
        '4':'el-icon-data-analysis'
      },
      isCollapse: false
    }
  },
  created() {
    this.getMenuDict()
  },
  methods: {
    // 点击按钮，切换菜单的折叠与展开
    toggleCollapse() {
      this.isCollapse = !this.isCollapse
    },
    // 获取所有菜单
    async getMenuDict() {
      console.log(JSON.parse(sessionStorage.getItem('menus')))
      this.menuDict = JSON.parse(sessionStorage.getItem('menus'))
    },
  }
}
</script>

<style lang="scss">
.el-submenu__title,.el-menu-item{
  i{
    color: inherit !important;
  }
}

.el-submenu__title:hover,.el-menu-item:hover{
  i{
    color: inherit !important;
  }
  span{
    color: inherit !important;
  }
}

.el-scrollbar {
  .el-scrollbar__view {
    height: 100%;
  }
}
.menu-info {
  .menu-contorl {
    line-height: 52px;
    font-size: 20px;
    display: table-cell;
    vertical-align: middle;
  }
}
</style>
