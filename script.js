// Gestion du changement Bac Général / Technique
document.addEventListener('DOMContentLoaded', function() {
    const bacGeneral = document.getElementById('bacGeneral');
    const bacTechnique = document.getElementById('bacTechnique');
    const seriesGenerales = document.getElementById('seriesGenerales');
    const seriesTechniques = document.getElementById('seriesTechniques');
    const matieresContainer = document.getElementById('matieresContainer');

    function toggleSeries() {
        if (bacGeneral.checked) {
            seriesGenerales.style.display = 'block';
            seriesTechniques.style.display = 'none';
            chargerMatieres('general');
        } else {
            seriesGenerales.style.display = 'none';
            seriesTechniques.style.display = 'block';
            chargerMatieres('technique');
        }
    }

    bacGeneral.addEventListener('change', toggleSeries);
    bacTechnique.addEventListener('change', toggleSeries);
    toggleSeries(); // initialisation

    // Charge les matières avec coefficient et note (exemple pour série générale)
    function chargerMatieres(type) {
        let html = '';
        const matieres = type === 'general' 
            ? ['Mathématiques', 'Physique-Chimie', 'SVT', 'Philosophie', 'Malagasy', 'Français', 'Anglais', 'Éducation physique et sportive', 'SES', 'Histoire-Géographie']
            : ['Comptabilité', 'Économie', 'Dessin Technique', 'Mécanique', 'Électronique'];
        
        matieres.forEach(matiere => {
            html += `<div class="matieres-ligne mb-2">
                        <span class="fw-bold">${matiere}</span>
                        <div>
                            <label>Coeff <input type="number" class="form-control form-control-sm d-inline-block input-coeff" value="1" min="0" step="0.5"></label>
                            <label>Note <input type="number" class="form-control form-control-sm d-inline-block input-note" value="" min="0" max="20" step="0.01"></label>
                            <span class="ms-2 fw-bold resultat-note">-</span>
                        </div>
                    </div>`;
        });
        matieresContainer.innerHTML = html;

        // Ajout des écouteurs pour calcul automatique
        document.querySelectorAll('.input-note, .input-coeff').forEach(input => {
            input.addEventListener('input', calculerNotePonderee);
        });
    }

    function calculerNotePonderee(e) {
        const ligne = e.target.closest('.matieres-ligne');
        const coeff = parseFloat(ligne.querySelector('.input-coeff').value) || 0;
        const note = parseFloat(ligne.querySelector('.input-note').value) || 0;
        const resultat = ligne.querySelector('.resultat-note');
        const ponderee = note * coeff;
        resultat.textContent = ponderee.toFixed(2);
    }

    // Vous pouvez ajouter ici toute la gestion des autres catégories (centres d'intérêt, etc.)
});