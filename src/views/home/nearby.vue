<template>
    <div class="nearby">
      <h3 class="nearby__title">附近店铺</h3>
      <router-link :to="`/shop/${item._id}`" v-for="item in nearbyList" :key="item._id">
      <shop-info :item="item" />
      </router-link>
    </div>
</template>

<script>
import { ref } from 'vue'
import { get } from '../../utils/request'
import shopInfo from '../../components/shopInfo'

const usernearbyList = () => {
  const nearbyList = ref([])
  const getNear = async () => {
    const result = await get('/api/shop/hot-list')
    if (result?.errno === 0 && result?.data?.length) {
      nearbyList.value = result.data
    }
  }
  return { nearbyList, getNear }
}
export default {
  name: 'Nearby',
  components: { shopInfo },
  setup () {
    const { nearbyList, getNear } = usernearbyList()
    getNear()
    return { nearbyList }
  }
}
</script>

<style lang="scss" scoped>
.nearby{
  &__title{
    margin: .16rem 0 .02rem 0;
    font-size: .18rem;
    color: #333;
    // font-weight: normal;
  }
  a{
    text-decoration: none;
  }
}
.gap{
  height: .1rem;
  background: #F1F1F1;
  margin: 0 -.18rem;
}
</style>
