<template>
  <div class="app-container">
    <el-card>
      <el-row :gutter="20">
        <el-col :span="36" :xs="24">
           <!-- 搜索框 -->
          <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px">
            <el-form-item label="账号" prop="userid">
              <el-input
                v-model="queryParams.id"
                placeholder="请输入账号"
                clearable
                size="small"
                style="width: 240px"
                @keyup.enter.native="handleQuery"
              />
            </el-form-item>
            <el-form-item label="姓名" prop="username">
              <el-input
                v-model="queryParams.username"
                placeholder="请输入姓名"
                clearable
                size="small"
                style="width: 240px"
                @keyup.enter.native="handleQuery"
              />
            </el-form-item>
            <el-form-item label="状态" prop="is_active">
<!--              数据库中状态一栏应是0或者1，这样才能根据:value修改状态栏-->
              <el-select
                v-model="queryParams.is_active"
                placeholder="请选择"
                clearable
                size="small"
                style="width: 240px"
              >
                <el-option
                  label="正常"
                  :value="1"
                />
                <el-option
                  label="停用"
                  :value="0"
                />
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
            <el-col :span="1.5">
              <el-button
                type="success"
                plain
                icon="el-icon-edit"
                size="mini"
                :disabled="single"
                @click="handleUpdate"
              >修改
              </el-button>
            </el-col>
            <el-col :span="1.5">
              <el-button
                type="danger"
                plain
                icon="el-icon-delete"
                size="mini"
                :disabled="multiple"
                @click="handleDelete"
              >删除
              </el-button>
            </el-col>
            <el-col :span="1.5">
              <el-button
                type="info"
                plain
                icon="el-icon-upload2"
                size="mini"
                @click="handleImport"
              >导入
              </el-button>
            </el-col>
            <el-col :span="1.5">
              <el-button
                type="warning"
                plain
                icon="el-icon-download"
                size="mini"
                @click="handleExport"
              >导出
              </el-button>
            </el-col>
          </el-row>
          <!--用户列表区域-->
          <el-table :data="userList" height="400" style="width: 100%" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="50" align="center" />
            <el-table-column key="id" sortable label="用户编号" align="center" prop="id" />
            <el-table-column
              key="username"
              label="用户账号"
              align="center"
              prop="username"
              :show-overflow-tooltip="true"
            />
            <el-table-column
              key="name"
              label="姓名"
              align="center"
              prop="name"
              :show-overflow-tooltip="true"
            />
            <el-table-column
              key="gender"
              label="性别"
              align="center"
              :show-overflow-tooltip="true"
            >
              <template slot-scope="scope">
                <span v-if="scope.row.gender">男</span>
                <span v-else>女</span>
              </template>
            </el-table-column>
            <el-table-column
              key="role"
              label="角色"
              align="center"
              :show-overflow-tooltip="true"
            >
              <template slot-scope="scope">
                <p v-for="item in scope.row.role_list">
                  {{ item }}
                </p>
              </template>
            </el-table-column>
            <el-table-column
              key="is_active"
              label="状态"
              align="center"
            >
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
              label="创建时间"
              align="center"
              prop="create_time"
              width="160"
            />
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
                />
                <el-button
                  v-if="scope.row.id !== 1"
                  size="mini"
                  type="danger"
                  icon="el-icon-delete"
                  @click="handleDelete(scope.row.id)"
                />
                <el-tooltip effect="light" content="重置" placement="bottom" :enterable="false">
                  <el-button
                    size="mini"
                    type="warning"
                    icon="el-icon-key"
                    @click="handleResetPwd(scope.row)"
                  />
                </el-tooltip>
              </template>
            </el-table-column>
          </el-table>
          <!--   分页区-->
          <div class="pagination-container">
            <el-pagination
              :current-page="queryParams.pageNum"
              :page-size="queryParams.pageSize"
              layout='total, prev, pager, next, jumper'
              :total="total"
              style="text-align: right;margin-top: 30px"
              @current-change="getList"/>
          </div>
          <!-- 分页区域 -->
          <!--          page	当前页数  支持 .sync 修饰符	-->
          <!--          limit	每页显示条目个数-->
          <pagination
            v-show="total>0"
            :total="total"
            :page.sync="queryParams.pageNum"
            :limit.sync="queryParams.pageSize"
            @pagination="getList"
          />
        </el-col>
      </el-row>
    </el-card>

  </div>
</template>

<script>
import { listUser } from '@/api/system/user'
import Pagination from '@/components/Pagination'
export default {
  name: 'User',
  components: { Pagination },
  data() {
    return {
      // 非单个禁用
      single: true,
      // 非多个禁用
      multiple: true,
      // 总条数
      total: 0,
      // 当前页
      // currentPage: 1,
      // 每页记录数
      // limit: 10,
      // 用户表格数据
      userList: null,
      // 状态数据字典
      statusOptions: [{ dictLabel: '正常', dictValue: true }, { dictLabel: '停用', dictValue: false }],
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        id: undefined,
        username: undefined,
        is_active: undefined
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    // 查询用户列表
    getList() {
      listUser(this.queryParams).then(res => {
        console.log(res)
        this.userList = res.results
        this.total = res.count
      })
    },
    handleQuery() {
      this.getList()
    },
    // 清空
    resetQuery() {
      // 1.表单输入项数据清空
      this.queryParams = {}
      // 2.查询所有讲师数据
      this.getList()
    },
    handleAdd() {
    },
    handleUpdate(row) {
    },
    handleDelete(id) {
    },
    handleExport() {
    },
    handleImport() {
    }
  }
}
</script>

<style scoped>

</style>
