<template>
  <div class="app-container">
    <el-form ref="queryForm" :model="queryParams" :inline="true">
      <el-form-item label="部门名称" prop="deptName">
        <el-input
          v-model="queryParams.deptName"
          placeholder="请输入部门名称"
          clearable
          size="small"
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="状态" prop="status">
        <el-select v-model="queryParams.status" placeholder="部门状态" clearable size="small">
          <el-option label="1" value="1"></el-option>
          <el-option label="0" value="0"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>
    <el-table
      :data="deptList"
      row-key="id"
      border
      default-expand-all
      :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
      <el-table-column prop="deptName" label="部门名称" />
      <el-table-column prop="orderNum" label="排序" width="200" />
      <el-table-column prop="status" label="状态"  width="200" />
      <el-table-column
        label="操作"
        align="center"
        class-name="small-padding fixed-width"
      >
        <template >
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
          >修改</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-plus"
          >新增</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'Dept',
  data() {
    return {
      queryParams: {
        deptName: '',
        status: ''
      },
      deptList: [
        {
          id: '1',
          deptName: '创新科技',
          orderNum: '1',
          status: '1',
          parentId: '0',
          children: [{
            id: '2',
            deptName: '北京分公司',
            orderNum: '1',
            status: '1',
            parentId: '1'
          }, {
            id: '3',
            deptName: '上海分公司',
            orderNum: '2',
            status: '1',
            parentId: '1'
          }, {
            id: '3',
            deptName: '上海分公司',
            orderNum: '2',
            status: '1',
            parentId: '1'
          }]
        }]
    }
  },
  methods: {
    /** 搜索按钮操作 */
    handleQuery() {
    },
    /** 重置按钮操作 */
    resetQuery() {
    }
  }
}
</script>

<style scoped>

</style>
