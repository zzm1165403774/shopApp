<template>
  <div class="wrapper">
    <div class="title">我的订单</div>
    <div class="orders">
      <div
        class="order"
        v-for="(item, index) in list"
        :key="index"
      >
        <div class="order__title">
          {{item.shopName}}
          <span class="order__status">{{item.isCanceled ? '已取消':'已下单'}}</span>
        </div>
        <div class="order__content">
          <div class="order__content__imgs">
            <template
             v-for="(inner, innerIndex) in item.products"
             :key="innerIndex"
            >
              <img
              class="order__content__img"
              :src="inner.product.img"
              v-if="innerIndex<=3"
              >
            </template>
          </div>
          <div class="order__content__info">
            <div class="order__content__info__price">&yen;36.88</div>
            <div class="order__content__info__count">共{{item.products.length}}件</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Docker :currentIndex ="2" />
</template>
<script>
import { get } from '../../utils/request'
import Docker from '../../components/docker'
import { reactive, toRefs } from 'vue'
const useOrderList = () => {
  const data = reactive({ list: [] })
  const getNear = async () => {
    const result = await get('/api/order')
    if (result?.errno === 0 && result?.data?.length) {
      data.list = result.data
    }
  }
  getNear()
  const { list } = toRefs(data)
  return { list }
}
export default {
  components: { Docker },
  name: 'orderList',
  setup () {
    const { list } = useOrderList()
    return { list }
  }
}
</script>
<style lang="scss" scoped>
.wrapper{
  position: absolute;
  left: 0;
  top: 0;
  bottom: .5rem;
  right: 0;
  overflow-y: auto;
  background-color: #eee;
}
.title{
  background-color: #fff;
  line-height: .44rem;
  font-size: .16rem;
  text-align: center;
}
.order{
  padding: .16rem;
  background-color: #fff;
  margin: .16rem .18rem;
  &__title{
    margin-bottom: .16rem;
    line-height: .22rem;
    font-size: .16rem;
    color: #333;
  }
  &__status{
    float: right;
    font-size: .14rem;
    color: #999;
  }
  &__content{
    display: flex;
    &__imgs{
      flex: 1;
    }
    &__img{
      width: .4rem;
      height: .4rem;
      margin-right: .12rem;
    }
    &__info{
      width: .7rem;
      &__price{
        margin-bottom: .04rem;
        font-size: .14rem;
        color: #e93b3b;
        line-height: .2rem;
        text-align: right;
      }
      &__count{
        font-size: .12rem;
        text-align: right;
        line-height: .14rem;
      }
    }
  }
}
</style>
