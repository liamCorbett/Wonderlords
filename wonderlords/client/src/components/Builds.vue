<template>
    <div class="container">
        <div>
            <div>
                <h1>Builds</h1>
                <hr><br>
                <button type="button">Copy link to build</button>
                <br><br>
                <table>
                    <tbody>
                        <tr>
                            <td></td>
                            <td v-for="(hero_class, class_index) in hero_classes" :key="class_index">{{hero_class}}</td>
                        </tr>
                        <tr v-for="(hero_race, race_index) in hero_races" :key="race_index">
                            <td>{{hero_race}}</td>
                            <td v-for="(hero_class2, class_index2) in hero_classes" :key="class_index2"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            hero_classes: [],
            hero_races: [],
        };
    },
    methods: {
        getHeroMatrix() {
            const hero_matrix_url = 'http://localhost:5000/hero_matrix';
        },
        getHeroClasses() {
            const hero_classes_url = 'http://localhost:5000/classes';
            
            axios.get(hero_classes_url)
                .then((response) => {
                    this.hero_classes = response.data;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        getHeroRaces() {
            const hero_races_url = 'http://localhost:5000/races';
            
            axios.get(hero_races_url)
                .then((response) => {
                    this.hero_races = response.data;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
    },
    created() {
        this.getHeroClasses();
        this.getHeroRaces();
    },
};
</script>