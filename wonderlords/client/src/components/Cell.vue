<template>
    <div>
        <!-- <button v-for="(unit, i) in units" :key="i" v-tooltip="unit">{{unit}}</button> -->
        <img v-if="!units" src="../assets/unit-img/default.jpg">
        <img v-for="(unit, i) in units" :key="i" :src="getUnitImg(unit)" :alt="unit" v-tooltip="getTooltip(unit)">
    </div>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    methods: {
        getUnitImg(unit) {
            return require('../assets/unit-img/'+unit+'.png');
        },
        getTooltip(unit) {
            return "<h5>" + unit + "</h5>";
        }
    },
    props: [
        'units'
    ],
    created() {

    },
};
</script>

<style>
    img {
        height: 100%;
        width: 100%;
    }
</style>
