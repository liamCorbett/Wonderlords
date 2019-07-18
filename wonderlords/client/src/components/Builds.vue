<template>
    <div class="container">
        <div>
            <div>
                <h1>Builds</h1>
                <hr><br>
                <button type="button">Show In-Game Icons</button>
                <button type="button">Rotate Display</button>
                <button type="button">Hide Unused</button>
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
                            <td v-for="(hero_class, class_index) in hero_classes" :key="class_index">
                                <cell :units="hero_matrix[race_index][class_index]"></cell>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Cell from './Cell';

export default {
    data() {
        return {
            hero_classes: [],
            hero_races: [],
            hero_matrix: [],
        };
    },
    methods: {
        getHeroMatrix() {
            const hero_matrix_url = 'http://localhost:5000/hero_matrix';

            axios.get(hero_matrix_url)
                .then((response) => {
                    this.hero_matrix = response.data;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
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
    components: {
        Cell,
    },
    created() {
        this.getHeroClasses();
        this.getHeroRaces();
        this.getHeroMatrix();
    },
};
</script>

<style>
table {
    background: rgba(80,80,80,0.4);
}
td {
    max-width: 180px;
    max-height: 180px;
    margin: 1px;
    padding: 0;
}
</style>
