<template>
    <div class="wrapper">
        <div class="search">
            <div @click="handleBack" class="search__back iconfont">&#xe677;</div>
            <div class="search__content">
                <span class="search__content__icon iconfont">&#xe60a;</span>
                <input
                 class="search__content__input"
                 placeholder="请输入商品名称"
                >
            </div>
        </div>
        <shop-info :item="data.item" :hideBorder="true" />
        <Content :shopName="data.item.name" />
    </div>
    <cart />
</template>
<style lang="scss" scoped>
.wrapper{
    padding: 0 .18rem;
}
.search{
    height: .32rem;
    margin: .14rem 0 .04rem 0;
    display: flex;
    &__back{
        width: .3rem;
        font-size: .24rem;
        color: #b6b6b6;
    }
    &__content{
        display: flex;
        flex: 1;
        background: #f5f5f5;
        border-radius: .16rem;
        &__icon{
            width: .44rem;
            text-align: center;
            color: #b7b7b7;
            padding-top: .07rem;
        }
        &__input{
            padding-right: .2rem;
            display: block;
            width: 100%;
            border: none;
            outline: none;
            background: none;
            font-size: .14rem;
            &::placeholder{
                color: #333;
            }
        }
    }
}
</style>
<script>
import { useRouter, useRoute } from 'vue-router'
import { reactive } from 'vue'
import shopInfo from '../../components/shopInfo.vue'
import { get } from '../../utils/request'
import Content from './content.vue'
import Cart from './cart'
const useShopInfo = () => {
  const route = useRoute()
  const data = reactive({
    item: {}
  })
  const getData = async () => {
    const result = await get(`/api/shop/${route.params.id}`)
    if (result?.errno === 0 && result?.data) {
      data.item = result.data
    }
  }
  return { data, getData }
}

export default {
  components: { shopInfo, Content, Cart },
  name: 'Shop',
  setup () {
    const router = useRouter()
    const { data, getData } = useShopInfo()
    getData()
    const handleBack = () => {
      router.back()
    }
    return { data, handleBack }
  }
}
</script>
