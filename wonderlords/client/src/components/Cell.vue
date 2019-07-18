<template>
    <div><button v-for="(unit, i) in units" :key="i">{{unit}}</button></div>
</template>

<script>
export default {
    data() {

    },
    methods: {

    },
    props: [
        'units'
    ],
    created() {

    }
}
</script>