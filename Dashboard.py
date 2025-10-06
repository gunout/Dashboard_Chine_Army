# dashboard_defense_chine_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - Chine",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé avec couleurs chinoises
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #DE2910, #FFDE00, #DE2910);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #DE2910, #FF6B35);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #DE2910;
        border-bottom: 3px solid #FFDE00;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .nuclear-card {
        background: linear-gradient(135deg, #8B0000, #DE2910);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .navy-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .air-force-card {
        background: linear-gradient(135deg, #0055B7, #0077CC);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .army-card {
        background: linear-gradient(135deg, #8B0000, #B22222);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .strategic-card {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .cyber-card {
        background: linear-gradient(135deg, #2d3436, #636e72);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .space-card {
        background: linear-gradient(135deg, #1a237e, #303f9f);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseChineDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.nuclear_arsenal = self.define_nuclear_arsenal()
        self.missile_systems = self.define_missile_systems()
        
    def define_branches_options(self):
        return [
            "Armée Populaire de Libération (APL)", "Forces Terrestres PLA", 
            "Marine PLA", "Force Aérienne PLA", "Force de Fusées PLA",
            "Force de Soutien Stratégique", "Garde Côtière", "Police Armée Populaire"
        ]
    
    def define_programmes_options(self):
        return [
            "Modernisation Militaire Intégrée", "Ceinture et Route Sécuritaire",
            "Supériorité Aérospatiale", "Marine Bleue", "Dissuasion Nucléaire",
            "Guerre Informatisée", "Intelligence Artificielle Militaire"
        ]
    
    def define_nuclear_arsenal(self):
        return {
            "DF-41": {"type": "ICBM", "portee": 15000, "ogives": 10, "statut": "Opérationnel"},
            "DF-31AG": {"type": "ICBM", "portee": 12000, "ogives": 3, "statut": "Opérationnel"},
            "DF-26": {"type": "IRBM", "portee": 4000, "ogives": "Conventionnelle/Nucléaire", "statut": "Opérationnel"},
            "JL-2": {"type": "SLBM", "portee": 8000, "ogives": 4, "statut": "Opérationnel"},
            "JL-3": {"type": "SLBM", "portee": 12000, "ogives": 6, "statut": "Déploiement"},
            "DF-ZF": {"type": "Missile Hypersonique", "portee": 2500, "ogives": 1, "statut": "Opérationnel"}
        }
    
    def define_missile_systems(self):
        return {
            "HQ-9": {"type": "Défense AA", "portee": 200, "cibles": "Aéronefs, missiles", "statut": "Opérationnel"},
            "HQ-19": {"type": "Défense AA/ABM", "portee": 300, "cibles": "BM, satellites", "statut": "Opérationnel"},
            "DF-17": {"type": "Missile Hypersonique", "portee": 1800, "vitesse": "Mach 5+", "statut": "Opérationnel"},
            "YJ-18": {"type": "Missile Anti-Navire", "portee": 500, "vitesse": "Mach 0.8-3.0", "statut": "Opérationnel"},
            "CJ-100": {"type": "Missile de Croisière", "portee": 2000, "vitesse": "Mach 3", "statut": "Déploiement"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour la Chine"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Tests_Missiles': self.simulate_missile_tests(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Artillerie': self.simulate_artillery_capacity(annees),
            'Couverture_AD': self.simulate_air_defense_coverage(annees),
            'Resilience_Logistique': self.simulate_logistical_resilience(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Armements': self.simulate_weapon_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'nucleaire' in config.get('priorites', []):
            data.update({
                'Stock_Ogives_Nucleaires': self.simulate_nuclear_arsenal_size(annees),
                'Portee_Max_Missiles_Km': self.simulate_missile_range_evolution(annees),
                'Tetes_Multiples': self.simulate_mirv_development(annees),
                'Essais_Souterrains': self.simulate_underground_tests(annees)
            })
        
        if 'modernisation' in config.get('priorites', []):
            data.update({
                'Nouveaux_Systemes': self.simulate_new_systems(annees),
                'Taux_Modernisation': self.simulate_modernization_rate(annees),
                'Exportations_Armes': self.simulate_weapon_exports(annees)
            })
        
        if 'aerospatial' in config.get('priorites', []):
            data.update({
                'Satellites_Militaires': self.simulate_military_satellites(annees),
                'Capacite_Antisatellite': self.simulate_antisatellite_capability(annees),
                'Defense_Aerospatiale': self.simulate_aerospace_defense(annees)
            })
        
        if 'cyber' in config.get('priorites', []):
            data.update({
                'Attaques_Cyber_Reussies': self.simulate_cyber_attacks(annees),
                'Reseau_Commandement_Cyber': self.simulate_cyber_command(annees),
                'Cyber_Defense_Niveau': self.simulate_cyber_defense(annees)
            })
        
        if 'marine' in config.get('priorites', []):
            data.update({
                'Navires_Combat': self.simulate_naval_vessels(annees),
                'Porte_Avions': self.simulate_aircraft_carriers(annees),
                'Sous_Marins_Attack': self.simulate_attack_submarines(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour la Chine"""
        configs = {
            "Armée Populaire de Libération (APL)": {
                "type": "armee_totale",
                "budget_base": 250.0,
                "personnel_base": 2000,
                "exercices_base": 200,
                "priorites": ["modernisation", "marine", "aerospatial", "cyber", "nucleaire"],
                "doctrines": ["Défense Active", "Guerre Informatisée", "Opérations au-delà du Premier Îlot"],
                "capacites_speciales": ["Forces de Réaction Rapide", "Guerre Électronique", "Cyber Guerre"]
            },
            "Force de Fusées PLA": {
                "type": "branche_strategique",
                "personnel_base": 120,
                "exercices_base": 30,
                "priorites": ["icbm", "df41", "hypersonique", "mirv"],
                "systemes_deployes": ["DF-41", "DF-31AG", "DF-26", "DF-ZF"],
                "zones_cibles": ["USA", "Asie-Pacifique", "Inde"]
            },
            "Marine PLA": {
                "type": "branche_navale",
                "personnel_base": 250,
                "exercices_base": 60,
                "priorites": ["porte_avions", "sous_marins", "mer_chine", "projection"],
                "flottes_principales": ["Flotte du Nord", "Flotte de l'Est", "Flotte du Sud"],
                "navires_cles": ["Porte-avions Type 003", "Destroyers Type 055", "Sous-marins Type 094"]
            },
            "Modernisation Militaire Intégrée": {
                "type": "programme_strategique",
                "budget_base": 80.0,
                "priorites": ["technologie", "formation", "equipement", "doctrine"],
                "objectifs": ["Armée mondiale de classe d'ici 2049"],
                "domaines_cles": ["IA militaire", "Guerre spatiale", "Cyberguerre"]
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 150,
            "exercices_base": 40,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec croissance chinoise"""
        budget_base = config.get('budget_base', 200.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.08 * (annee - 2000))  # Croissance rapide
            # Accélération selon périodes
            if 2008 <= annee <= 2012:  # Post-Olympiques
                base *= 1.20
            elif 2013 <= annee <= 2017:  # Initiative Ceinture et Route
                base *= 1.25
            elif annee >= 2018:  # Modernisation accélérée
                base *= 1.30
            elif annee >= 2022:  # Tensions géopolitiques
                base *= 1.35
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs avec professionnalisation"""
        personnel_base = config.get('personnel_base', 2200)
        # Réduction progressive avec professionnalisation
        return [personnel_base * (1 - 0.005 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [1.7 + 0.15 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec complexité croissante"""
        base = config.get('exercices_base', 150)
        return [base + 8 * (annee - 2000) + 15 * np.sin(2 * np.pi * (annee - 2000)/3) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 60 + 2.0 * (annee - 2000)  # Amélioration rapide
            if annee >= 2008:  # Réformes post-Olympiques
                base += 15
            if annee >= 2015:  # Modernisation accélérée
                base += 12
            if annee >= 2020:  # Expérience opérationnelle
                base += 8
            readiness.append(min(base, 92))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            base = 70  # Départ plus bas mais croissance rapide
            if annee >= 2008:
                base += 3  # Investissements stratégiques
            if annee >= 2015:
                base += 8  # Systèmes avancés
            if annee >= 2020:
                base += 7  # Hypersoniques et capacités spatiales
            deterrence.append(min(base, 95))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(45 - 1.2 * (annee - 2000), 10) for annee in annees]
    
    def simulate_missile_tests(self, annees):
        """Tests de missiles"""
        tests = []
        for annee in annees:
            if annee < 2010:
                tests.append(3)
            elif annee < 2015:
                tests.append(8 + (annee - 2010))
            elif annee < 2020:
                tests.append(15 + 2 * (annee - 2015))
            else:
                tests.append(25 + 3 * (annee - 2020))
        return tests
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(60 + 2.5 * (annee - 2000), 94) for annee in annees]
    
    def simulate_artillery_capacity(self, annees):
        """Capacité d'artillerie"""
        return [min(85 + 0.8 * (annee - 2000), 96) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        return [min(60 + 2.8 * (annee - 2000), 94) for annee in annees]
    
    def simulate_logistical_resilience(self, annees):
        """Résilience logistique"""
        return [min(70 + 2.2 * (annee - 2000), 93) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(75 + 3.2 * (annee - 2000), 96) for annee in annees]
    
    def simulate_weapon_production(self, annees):
        """Production d'armements (indice)"""
        return [min(70 + 3.0 * (annee - 2000), 97) for annee in annees]
    
    def simulate_nuclear_arsenal_size(self, annees):
        """Évolution du stock d'ogives nucléaires"""
        stock = []
        for annee in annees:
            if annee < 2010:
                stock.append(200 + 10 * (annee - 2000))
            elif annee < 2020:
                stock.append(300 + 25 * (annee - 2010))
            else:
                stock.append(550 + 50 * (annee - 2020))
        return [min(s, 1500) for s in stock]
    
    def simulate_missile_range_evolution(self, annees):
        """Évolution de la portée maximale des missiles"""
        portee = []
        for annee in annees:
            if annee < 2010:
                portee.append(8000)
            elif annee < 2015:
                portee.append(10000 + 500 * (annee - 2010))
            elif annee < 2020:
                portee.append(12000 + 600 * (annee - 2015))
            else:
                portee.append(15000)  # DF-41 opérationnel
        return portee
    
    def simulate_mirv_development(self, annees):
        """Développement des têtes multiples"""
        return [min(1 + 0.8 * (annee - 2000), 10) for annee in annees]
    
    def simulate_underground_tests(self, annees):
        """Essais souterrains et préparation"""
        return [min(70 + 1.5 * (annee - 2000), 95) for annee in annees]
    
    def simulate_new_systems(self, annees):
        """Nouveaux systèmes déployés"""
        return [min(3 + 3 * (annee - 2000), 60) for annee in annees]
    
    def simulate_modernization_rate(self, annees):
        """Taux de modernisation des équipements"""
        return [min(20 + 5 * (annee - 2000), 90) for annee in annees]
    
    def simulate_weapon_exports(self, annees):
        """Exportations d'armes (milliards USD)"""
        return [min(1 + 0.8 * (annee - 2000), 12) for annee in annees]
    
    def simulate_military_satellites(self, annees):
        """Satellites militaires en orbite"""
        return [min(20 + 8 * (annee - 2000), 120) for annee in annees]
    
    def simulate_antisatellite_capability(self, annees):
        """Capacité antisatellite"""
        return [min(50 + 4 * (annee - 2000), 92) for annee in annees]
    
    def simulate_aerospace_defense(self, annees):
        """Défense aérospatiale"""
        return [min(65 + 3.0 * (annee - 2000), 93) for annee in annees]
    
    def simulate_cyber_attacks(self, annees):
        """Attaques cyber réussies (estimation)"""
        return [min(15 + 4 * (annee - 2000), 120) for annee in annees]
    
    def simulate_cyber_command(self, annees):
        """Réseau de commandement cyber"""
        return [min(70 + 2.8 * (annee - 2000), 94) for annee in annees]
    
    def simulate_cyber_defense(self, annees):
        """Capacités de cyber défense"""
        return [min(65 + 3.0 * (annee - 2000), 92) for annee in annees]
    
    def simulate_naval_vessels(self, annees):
        """Nombre de navires de combat"""
        return [min(200 + 15 * (annee - 2000), 350) for annee in annees]
    
    def simulate_aircraft_carriers(self, annees):
        """Porte-avions en service"""
        carriers = []
        for annee in annees:
            if annee < 2012:
                carriers.append(0)
            elif annee < 2019:
                carriers.append(1)
            elif annee < 2025:
                carriers.append(2)
            else:
                carriers.append(3)
        return carriers
    
    def simulate_attack_submarines(self, annees):
        """Sous-marins d'attaque"""
        return [min(40 + 3 * (annee - 2000), 80) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🐉 ANALYSE STRATÉGIQUE AVANCÉE - RÉPUBLIQUE POPULAIRE DE CHINE</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #DE2910, #FFDE00); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🛡️ SYSTÈME DE DÉFENSE INTÉGRÉ DE L\'ARMÉE POPULAIRE DE LIBÉRATION</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et stratégiques (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Analyse Branche Militaire", "Programmes Stratégiques", "Vue Systémique", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Analyse Branche Militaire":
            selection = st.sidebar.selectbox("Branche militaire:", self.branches_options)
        elif type_analyse == "Programmes Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        elif type_analyse == "Vue Systémique":
            selection = "Armée Populaire de Libération (APL)"
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_doctrinal = st.sidebar.checkbox("Analyse doctrinale", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Statut Quo", "Conflit Taïwan", "Modernisation Accélérée", "Confrontation USA"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_doctrinal': show_doctrinal,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.1f} Md$</h2>
                <p>📈 {:.1f}% du PIB</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ Professionnalisation en cours</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers']), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="nuclear-card">
                <h4>☢️ FORCE DE DISSUASION</h4>
                <h2>{:.0f}%</h2>
                <p>🚀 {} ogives stratégiques</p>
            </div>
            """.format(data_actuelle['Capacite_Dissuasion'], 
                     int(data_actuelle.get('Stock_Ogives_Nucleaires', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="strategic-card">
                <h4>🎯 TECHNOLOGIES AVANCÉES</h4>
                <h2>{:.0f}%</h2>
                <p>⚡ {} systèmes déployés</p>
            </div>
            """.format(data_actuelle['Developpement_Technologique'], 
                     int(data_actuelle.get('Nouveaux_Systemes', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_ad = ((data_actuelle['Couverture_AD'] - data_2000['Couverture_AD']) / 
                           data_2000['Couverture_AD']) * 100
            st.metric(
                "🛡️ Défense Anti-Aérienne",
                f"{data_actuelle['Couverture_AD']:.1f}%",
                f"{croissance_ad:+.1f}%"
            )
        
        with col7:
            if 'Portee_Max_Missiles_Km' in df.columns:
                croissance_portee = ((data_actuelle['Portee_Max_Missiles_Km'] - data_2000.get('Portee_Max_Missiles_Km', 8000)) / 
                                   data_2000.get('Portee_Max_Missiles_Km', 8000)) * 100
                st.metric(
                    "🎯 Portée Missiles Max",
                    f"{data_actuelle['Portee_Max_Missiles_Km']:,.0f} km",
                    f"{croissance_portee:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Couverture_AD']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Défense Anti-Aérienne']
            couleurs = ['#DE2910', '#FFDE00', '#2d3436', '#1a237e']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des programmes stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Stock_Ogives_Nucleaires' in df.columns:
                strategic_data.append(df['Stock_Ogives_Nucleaires'] / 10)  # Normalisation
                strategic_names.append('Stock Ogives (x10)')
            
            if 'Tests_Missiles' in df.columns:
                strategic_data.append(df['Tests_Missiles'])
                strategic_names.append('Tests de Missiles')
            
            if 'Nouveaux_Systemes' in df.columns:
                strategic_data.append(df['Nouveaux_Systemes'])
                strategic_names.append('Nouveaux Systèmes')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🚀 PROGRAMMES STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Cartes des zones d'intérêt
            st.markdown("""
            <div class="nuclear-card">
                <h4>🎯 ZONES D'INTÉRÊT STRATÉGIQUE</h4>
                <p><strong>Mer de Chine Méridionale:</strong> Revendications souveraineté</p>
                <p><strong>Détroit de Taïwan:</strong> Réunification prioritaire</p>
                <p><strong>Ceinture et Route:</strong> Sécurisation routes commerciales</p>
                <p><strong>Asie-Pacifique:</strong> Influence régionale croissante</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="strategic-card">
                <h4>🌐 RELATIONS INTERNATIONALES</h4>
                <p><strong>USA:</strong> Rivalité stratégique</p>
                <p><strong>Russie:</strong> Partenariat stratégique</p>
                <p><strong>Inde:</strong> Concurrence régionale</p>
                <p><strong>ASEAN:</strong> Influence économique</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Analyse des tensions
            tensions_data = {
                'Année': [2001, 2008, 2012, 2016, 2020, 2022, 2023],
                'Événement': ['EP-3', 'Jeux Pékin', 'Senkaku', 'Cour Permanente', 'COVID', 'Visite Pelosi', 'Survol Ballon'],
                'Niveau Tension': [6, 3, 7, 6, 8, 8, 7]  # sur 10
            }
            tensions_df = pd.DataFrame(tensions_data)
            
            fig = px.bar(tensions_df, x='Année', y='Niveau Tension', 
                        title="📈 ÉVOLUTION DES TENSIONS GÉOPOLITIQUES",
                        labels={'Niveau Tension': 'Niveau de Tension'},
                        color='Niveau Tension',
                        color_continuous_scale='reds')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Croissance économique et militaire
            croissance = [min(8 + 0.5 * (annee - 2000), 12) for annee in df['Annee']]
            fig = px.area(x=df['Annee'], y=croissance,
                         title="📈 CROISSANCE ÉCONOMIQUE SOUTENANT LA PUISSANCE MILITAIRE",
                         labels={'x': 'Année', 'y': 'Croissance PIB (%)'})
            fig.update_traces(fillcolor='rgba(222, 41, 16, 0.3)', line_color='#DE2910')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['DF-41', 'J-20', 'Type 055', 'DF-17', 
                           'Sous-marin Type 096', 'Porte-avions Type 003'],
                'Portée (km)': [15000, 2000, 0, 1800, 0, 0],
                'Année Service': [2019, 2017, 2020, 2020, 2025, 2022],
                'Statut': ['Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Développement', 'Opérationnel']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée (km)', y='Année Service', 
                           size='Portée (km)', color='Statut',
                           hover_name='Système', log_x=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES D'ARMES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la modernisation navale
            naval_data = {
                'Type Navire': ['Destroyers', 'Frégates', 'Corvettes', 'Sous-marins', 'Porte-avions'],
                '2000': [20, 40, 50, 60, 0],
                '2027': [45, 55, 70, 80, 3]
            }
            naval_df = pd.DataFrame(naval_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2000', x=naval_df['Type Navire'], y=naval_df['2000'],
                                marker_color='#1e3c72'))
            fig.add_trace(go.Bar(name='2027', x=naval_df['Type Navire'], y=naval_df['2027'],
                                marker_color='#DE2910'))
            
            fig.update_layout(title="🚢 EXPANSION DE LA MARINE CHINOISE",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Cartographie des installations
            st.markdown("""
            <div class="strategic-card">
                <h4>🗺️ INSTALLATIONS STRATÉGIQUES CLÉS</h4>
                <p><strong>Qingdao:</strong> QG Flotte du Nord</p>
                <p><strong>Sanya:</strong> Base sous-marine</p>
                <p><strong>Jiuquan:</strong> Cosmodrome</p>
                <p><strong>Xiangshan:</strong> QG Force de Fusées</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_doctrinal_analysis(self, config):
        """Analyse doctrinale avancée"""
        st.markdown('<h3 class="section-header">📚 ANALYSE DOCTRINALE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="nuclear-card">
                <h4>🎯 DOCTRINE DE DÉFENSE ACTIVE</h4>
                <p><strong>Dissuasion crédible:</strong> Force nucléaire minimale</p>
                <p><strong>Défense périphérique:</strong> Mer de Chine</p>
                <p><strong>Contrôle maritime:</strong> Premier et deuxième îlot</p>
                <p><strong>Riposte proportionnée:</strong> Escalade contrôlée</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="strategic-card">
                <h4>⚡ DOCTRINE DE GUERRE INFORMATISÉE</h4>
                <p><strong>Intégration systèmes:</strong> C4ISR avancé</p>
                <p><strong>Supériorité information:</strong> Domination cognitive</p>
                <p><strong>Cyber guerre:</strong> Actions numériques</p>
                <p><strong>Guerre électronique:</strong> Paralysie adverse</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="space-card">
                <h4>🛡️ STRATÉGIE AÉROSPATIALE</h4>
                <p><strong>Contrôle spatial:</strong> Satellites militaires</p>
                <p><strong>Défense antimissile:</strong> Bouclier intégré</p>
                <p><strong>Réseaux C4ISR:</strong> Commandement unifié</p>
                <p><strong>Mobilité stratégique:</strong> Projection de puissance</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Principes opérationnels
        st.markdown("""
        <div class="navy-card">
            <h4>🎖️ PRINCIPES OPÉRATIONNELS DE L'APL</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Guerre populaire moderne:</strong> Mobilisation nationale</div>
                <div><strong>• Victoire par la technologie:</strong> Supériorité qualitative</div>
                <div><strong>• Opérations conjointes:</strong> Coordination interarmes</div>
                <div><strong>• Initiative stratégique:</strong> Prise de contrôle</div>
                <div><strong>• Flexibilité opérationnelle:</strong> Adaptation rapide</div>
                <div><strong>• Soutien logistique:</strong> Chaîne d'approvisionnement</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Intervention USA Taïwan', 'Blocus Maritime', 'Guerre Cyber', 
                                 'Encerclement Stratégique', 'Instabilité Corée', 'Sanctions Économiques'],
                'Probabilité': [0.7, 0.5, 0.9, 0.6, 0.4, 0.8],
                'Impact': [0.9, 0.8, 0.7, 0.7, 0.6, 0.8],
                'Niveau Préparation': [0.8, 0.7, 0.9, 0.6, 0.5, 0.7]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Conflit Taïwan', 'Crise Nucléaire', 'Guerre Cyber', 
                           'Blocus Économique', 'Intervention USA'],
                'Dissuasion': [0.8, 0.9, 0.4, 0.6, 0.8],
                'Défense': [0.9, 0.5, 0.8, 0.7, 0.8],
                'Riposte': [0.95, 1.0, 0.9, 0.8, 0.9]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Dissuasion', x=response_df['Scénario'], y=response_df['Dissuasion']),
                go.Bar(name='Défense', x=response_df['Scénario'], y=response_df['Défense']),
                go.Bar(name='Riposte', x=response_df['Scénario'], y=response_df['Riposte'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR SCÉNARIO",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="nuclear-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Modernisation nucléaire:</strong> Triade crédible</div>
                <div><strong>• Contrôle maritime:</strong> Marine bleue</div>
                <div><strong>• Capacités conventionnelles:</strong> Forces rapides</div>
                <div><strong>• Guerre électronique:</strong> Supériorité spectrale</div>
                <div><strong>• Cyber défense:</strong> Résilience numérique</div>
                <div><strong>• Coopération stratégique:</strong> Partenariats sélectifs</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_nuclear_database(self):
        """Base de données des systèmes nucléaires"""
        st.markdown('<h3 class="section-header">☢️ BASE DE DONNÉES DES SYSTÈMES STRATÉGIQUES</h3>', 
                   unsafe_allow_html=True)
        
        nuclear_data = []
        for nom, specs in self.nuclear_arsenal.items():
            nuclear_data.append({
                'Système': nom,
                'Type': specs['type'],
                'Portée (km)': specs['portee'],
                'Ogives': specs['ogives'],
                'Statut': specs['statut'],
                'Classification': 'Offensif' if specs['type'] in ['ICBM', 'SLBM'] else 'Défensif'
            })
        
        nuclear_df = pd.DataFrame(nuclear_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.scatter(nuclear_df, x='Portée (km)', y='Ogives',
                           size='Portée (km)', color='Classification',
                           hover_name='Système', log_x=True,
                           title="☢️ CARACTÉRISTIQUES DES SYSTÈMES NUCLÉAIRES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="nuclear-card">
                <h4>📋 INVENTAIRE STRATÉGIQUE</h4>
            """, unsafe_allow_html=True)
            
            for systeme in nuclear_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{systeme['Système']}</strong><br>
                    🎯 {systeme['Type']} • 🚀 {systeme['Portée (km)']:,} km<br>
                    💣 {systeme['Ogives']} ogives • {systeme['Statut']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "📚 Doctrine Militaire",
            "⚠️ Évaluation Menaces",
            "☢️ Systèmes Stratégiques",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            if controls['show_doctrinal']:
                self.create_doctrinal_analysis(config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_technical']:
                self.create_nuclear_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - RÉPUBLIQUE POPULAIRE DE CHINE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="nuclear-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>📈 Croissance Économique</strong>
                        <p>Base économique solide soutenant la modernisation militaire</p>
                    </div>
                    <div class="navy-card" style="margin: 0.5rem 0;">
                        <strong>🚢 Expansion Navale</strong>
                        <p>Marine en croissance rapide avec capacités de projection</p>
                    </div>
                    <div class="air-force-card" style="margin: 0.5rem 0;">
                        <strong>🛡️ Technologies Avancées</strong>
                        <p>Systèmes hypersoniques et capacités spatiales en développement</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Initiative Diplomatique</strong>
                        <p>Influence croissante par la diplomatie et initiatives économiques</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="strategic-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>💧 Dépendance Énergétique</strong>
                        <p>Importations cruciales de pétrole et gaz</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>🌊 Tensions Maritimes</strong>
                        <p>Conflits territoriaux en mer de Chine</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>🤝 Rivalités Régionales</strong>
                        <p>Relations complexes avec voisins et USA</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Expérience Opérationnelle</strong>
                        <p>Forces peu expérimentées en combat réel</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🚀 DOMAINE NUCLÉAIRE</h5>
                    <p>• DF-41 pleinement opérationnel<br>• SLBM JL-3 déployé<br>• Bombardier H-20<br>• Ogives hypersoniques</p>
                </div>
                <div>
                    <h5>🛡️ EXPANSION NAVALE</h5>
                    <p>• 4-5 porte-avions<br>• Sous-marins Type 096<br>• Destroyers nouvelle génération<br>• Base outre-mer</p>
                </div>
                <div>
                    <h5>💻 DOMAINE CYBER/ESPACE</h5>
                    <p>• Station spatiale militaire<br>• IA militaire opérationnelle<br>• Guerre électronique avancée<br>• Réseaux quantiques</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="nuclear-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ DÉFENSE ACTIVE</h5>
                    <p>• Modernisation continue des forces<br>
                    • Renforcement capacités navales<br>
                    • Développement des systèmes hypersoniques<br>
                    • Sécurisation routes commerciales</p>
                </div>
                <div>
                    <h5>⚡ DIPLOMATIE STRATÉGIQUE</h5>
                    <p>• Résolution pacifique différends<br>
                    • Coopération économique régionale<br>
                    • Partenariats technologiques<br>
                    • Influence soft power</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseChineDashboardAvance()
    dashboard.run_advanced_dashboard()