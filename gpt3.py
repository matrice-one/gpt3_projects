import os
import openai
import pandas as pd

openai.api_key = "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"

restart_sequence = "\n"

df = pd.read_excel('/Users/neigelinerivollat/Desktop/RA_TA_Fall_21/NLP_Project/reduced_fr_df.xlsx)
df.head()


# FOR EACH ROW IN dF
    # FUNCTION TO OUTPUT ANSWER = 
        response = openai.Completion.create(
        engine="davinci",
        prompt="The following is a list of companies and the categories they fall into\nVoici une liste des fondations et leur domaine d'activité associé\n\ndevenir proprietaire de la collection dart chinois et japonais de monsieur et madame alfred baur-duret;  administrer, entretenir et completer la dite collection dart, mettre celle-ci a la disposition du public genevois notamment au moyen dexpositions, le tout conformement a larticle 8 du present acte de fondation;  devenir proprietaire de biens mobiliers et immobiliers pour permettre la pleine realisation du but designe ci-dessus, sous chiffre 2): art et culture.\n\npromouvoir et encourager le developpement et lepanouissement de la jeunesse et des personnes a mobilite reduite dans les domaines du sport, de la culture, de la formation et de leducation. la fondation poursuit egalement des buts caritatifs. a cette fin, elle peut notamment financer et/ou participer aux actions suivantes: 1. soutenir financierement des projets de construction ou de renovation dinstallations ou dinfrastructures, subventionnees ou pas, destines a la pratique du sport, a la culture, a la formation ou a leducation; 2. octroyer des bourses detudes dans les domaines du sport, de la culture et de lacademie; 3. soutenir financierement des personnes a mobilite reduite; 4. soutenir financierement des sportifs meritants; 5. soutenir des actions humanitaires. elle ne poursuite aucun but lucratif. le capital et leventuel benefice resultant de sa gestion sont exclusivement et irrevocablement affectes au but figurant a larticle 5 ci-dessus. elle na en particulier aucune activite commerciale. en cas dactivite financiere, soit la gestion du capital de la fondation, le produit sera affecte exclusivement a la realisation de ses buts. cette activite ne peut ^etre quaccessoire et ne sera pas en concurrence avec des institutions non-exonerees. : sports.\n\napporter une aide a lh^opital, site de saint-imier, ou a dautres etablissements dans le domaine medical et apparente, situes dans le jura bernois ou dans les districts limitrophes, ou actifs dans ces regions; elle peut egalement verser des bourses pour la recherche. au moins les 2/3 des montants verses par la fondation devront ^etre affectes a saint-imier ou dans le district de courtelary et le solde dans les autres districts ou regions limitrophes.: santé\n\nla fondation a pour but de reunir des amis du cheval et des pratiquants du sport equestre, de maintenir les traditions equestres, de developper la pratique de lequitation, notamment en contribuant a lorganisation de cours, de manifestations, de sorties en commun, de conferences (pour but complet cf. acte de fondation): sport\n\nmise a disposition de son chalet pour des rencontres ou des sejours organises par des familles, institutions ou associations. elle favorise les demarches sociales, formatives ou educatives. elle pr^ete gratuitement le chalet aux organisateurs des sejours de colonies de vacances de la paroisse catholique destavayer-le-lac. la fondation ne poursuit pas de but lucratif ou commercial.: religion\n\nassurer, au moins tous les deux ans, lorganisation dune manifestation sportive, destinee a promouvoir la gymnastique.: sport\n\neffectuer des dons sous forme de versements annuels aux personnes morales suivantes: 1) la fondation pasteur, suisse, 2) linstitut de cancerologie gustave roussy, a villejuif (france), 3) la croix-rouge francaise, 4) la croix-rouge suisse, 5) la commune de villeneuve (vaud, suisse), 6) la paroisse catholique de villeneuve (vaud, suisse), 7) la paroisse protestante de villeneuve (vaud, suisse), 8) la commune de pont-de-vaux (ain, france), 9) lhospice de pont-de-vaux (ain, france)(cf. statuts pour but complet). la fondation na pas de but lucratif et ne vise aucun gain.: religion\n\nsoutenir la recherche sur le cancer du poumon et ses metastases; comprehension, mecanisme de developpement et traitement (cf. statuts pour but complet): sante\n" + row_i,
        temperature=0,
        max_tokens=6,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
        )
    ## APPEND ANSWER TO ROW ANSWER COLUMN


## NEEDED = TRANSLATED VERSION (OR AT LEAST SAYING LANGUAGE)