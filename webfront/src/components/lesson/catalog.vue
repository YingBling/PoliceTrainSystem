<template>
  <el-card class="box-card">
    <el-tree :data="data" :props="Props" @node-click="handleNodeClick"></el-tree>
  </el-card>
</template>

<script>
export default {
  name: "catalog",
  data() {
    return {
      data: [{
        label: {
          name: '测试',
          url: ''
        },
        children: [
          {
            label: {
              name: 'big_buck_bunny',
              url: '12312312'
            }
            // }, {
            //   label: '乐高大电影2',
            //   url: ''
            // },
            // {
            //   label: '紧急救援',
            //   url: ''
            // }, {
            //   label: 'trailer',
            //   url: ''
            // }, {
            //   label: 'marvel',
            //   url: ''
            //
          },

        ]
      }],
      Props: {
        children: 'children',
        label: (data, node) => {
          return data.label.name
        }
      }
    };
  },
  methods: {
    handleNodeClick(data, node, obj) {
      /*
      data:结点的属性
      node:结点的data属性
      obj:调用的对象
       */
      // console.log(node)
      // console.log(data)
      // console.log(obj)
      if (node.level === 1) {
        console.log('level1')
      } else {
        console.log(data.label.url)
      }
    }
  }

}
</script>
<style scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 400px;
  height: 480px;

}
</style>
