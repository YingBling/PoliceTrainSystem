<template>
  <div class="app-container">
    <!--  面包屑导航-->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <!--      <el-breadcrumb-item v-for="(item,i) in data" :key="item" :to="getPath(i)">{{item}}</el-breadcrumb-item>-->
      <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!--  卡片视图区域-->
    <span>{{ this.$route.query.name }}</span>
    <el-card>
      <el-row :gutter="20">

        <!-- 搜索框 -->
        <el-col :span="36" :xs="24">
          <el-form :inline="true" label-width="68px">
            <el-form-item prop="userid">
              <el-input
                placeholder="查询关键字"
                clearable
                v-model="keyword"
                size="small"
                style="width: 240px"
                @keyup.enter.native="handleQuery"
              />
            </el-form-item>
            <el-form-item label="状态" prop="is_active">
              <el-select
                placeholder="请选择"
                clearable
                size="small"
                style="width: 240px"
              >
                <el-option label="启动" value="on"></el-option>
                <el-option label="禁用" value="off"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
              <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
            </el-form-item>
          </el-form>
          <!--增删改导入按钮-->
          <el-row :gutter="10" class="mb8">
            <el-col :span="1.5">
              <el-button
                type="primary"
                plain
                icon="el-icon-plus"
                size="mini"
                @click="handleAdd"
              >新增
              </el-button>
            </el-col>
          </el-row>
          <!--用户列表区域-->
          <el-table :data="filter_data" @selection-change="handleSelectionChange" height="400" style="width: 100%">
            <el-table-column type="selection" width="50" align="center"/>
            <el-table-column sortable key="id" label="用户编号" align="center" prop="id"/>
            <el-table-column
              key="username" label="用户账号" align="center" prop="username"
              :show-overflow-tooltip="true"
            />
            <el-table-column key="name" label="姓名"
                             align="center"
                             prop="name"
                             :show-overflow-tooltip="true"
            />
            <el-table-column key="gender" label="性别"
                             align="center"
                             :show-overflow-tooltip="true"
            >
              <template slot-scope="scope">
                <span v-if="scope.row.gender">男</span>
                <span v-else>女</span>
              </template>
            </el-table-column>
            <el-table-column key="role" label="角色"
                             align="center"
                             :show-overflow-tooltip='true'
            >
              <template slot-scope="scope">
                <p v-for="item in scope.row.role_list">
                  {{ item }}
                </p>
              </template>

            </el-table-column>
            <el-table-column
              key="is_active" label="状态" align="center">
              <template slot-scope="scope">
                <!--              scope.row代表该行所有数据-->
                <el-switch
                  v-model="scope.row.is_active"
                  disabled
                  @change="handleStatusChange(scope.row)"
                />
              </template>
            </el-table-column>
            <el-table-column
              label="创建时间" align="center" prop="create_time" width="160">
            </el-table-column>
            <el-table-column
              label="操作"
              align="center"
              width="180"
              fixed="right"
              class-name="small-padding fixed-width"
            >
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="primary"
                  icon="el-icon-edit"
                  @click="handleUpdate(scope.row)"
                >
                </el-button>
                <el-button
                  v-if="scope.row.id !== 1"
                  size="mini"
                  type="danger"
                  icon="el-icon-delete"
                  @click="handleDelete(scope.row)"
                >
                </el-button>
                <el-tooltip effect="light" content="重置" placement="bottom" :enterable="false">
                  <el-button
                    size="mini"
                    type="warning"
                    icon="el-icon-key"
                    @click="handleResetPwd(scope.row)"
                  >
                  </el-button>
                </el-tooltip>
              </template>
            </el-table-column>


          </el-table>


          <!-- 分页区域 -->
          <el-pagination
            style="position: center"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            @next-click="handleNextClick"
            @prev-click="handlePreClick"
            :current-page="query_params.page.current"
            :page-sizes="[1,2,5,10]"
            :page-size="query_params.page.size"
            layout="total, sizes, prev, pager, next, jumper"
            :total="query_params.page.total"
          >
          </el-pagination>
        </el-col>
      </el-row>

    </el-card>
  </div>
</template>

<script>
export default {
  name: "user",
  data() {
    return {
      keyword: '',
      query_params: {
        // 总页面数
        page: {
          "total": null,
          // 当前所在页
          "current": null,
          // 页面大小
          "size": 5,
        },
        ordering: 'id',
        name: null
      },
      userdata: [],
      filter_data:[]
    }
  },
  watch: {
    // userdata: {
    //   handler(val) {
    //     this.filter_data = this.userdata.results
    //   }
    // },
    keyword: {
      immediate: true,
      handler(val) {
        this.filter_data = this.userdata.results.filter((p) => {
          return p.name.indexOf(val) !== -1
        })
      }
    }
  },
  created() {
    this.get_all_users()
  },
  methods: {
    get_all_users() {
      this.$axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/rbac/user/',
        params: {
          'size': this.query_params.page.size,
          'page': this.query_params.page.current,
          'ordering': this.query_params.ordering,
          'name': this.query_params.name
        },
        headers: {
          Authorization: `Bearer ${sessionStorage.getItem('access')}`
        }
      })
        .then(res => {
          this.userdata = res.data
          this.query_params.page.total = this.userdata['count']
        })
    },
    handleQuery() {
    },
    handleSizeChange(size) {
      // 改变页面大小
      this.query_params.page.size = size
      this.get_all_users()
    },
    handleCurrentChange(current) {
      // 改变页码
      this.query_params.page.current = current
      this.get_all_users()
    },
    handlePreClick() {
      this.$axios({
        method: 'get',
        url: this.userdata['previous'],
        headers: {
          Authorization: `Bearer ${sessionStorage.getItem('access')}`
        }
      })
        .then(res => {
          this.userdata = res.data
          console.log(this.userdata)
          this.query_params.page.total = this.userdata['count']
        })

    },
    handleNextClick() {
      this.$axios({
        method: 'get',
        url: this.userdata['next'],
        headers: {
          Authorization: `Bearer ${sessionStorage.getItem('access')}`
        }
      })
        .then(res => {
          this.userdata = res.data
          this.query_params.page.total = this.userdata['count']
        })
    }
  },
}
</script>

<style lang="scss" scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>
